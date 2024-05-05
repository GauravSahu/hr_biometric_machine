# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

from datetime import datetime, timedelta
from zklib import zklib  # pip install zlib

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    emp_code = fields.Char("Emp Code")
    category = fields.Char("Category")


class BiometricMachine(models.Model):
    _name = 'biometric.machine'

    name = fields.Char("Machine IP")
    ref_name = fields.Char("Location")
    port = fields.Integer("Port Number")
    address_id = fields.Many2one("res.partner", 'Working Address')
    company_id = fields.Many2one("res.company", "Company Name")
    atten_ids = fields.One2many('biometric.data', 'mechine_id', 'Attendance')

    def download_attendance(self):
        for record in self:
            machine_ip = record.name
            port = record.port
            zk = zklib.ZKLib(machine_ip, int(port))
            res = zk.connect()
            if res:
                zk.enableDevice()
                zk.disableDevice()
                attendance = zk.getAttendance()
                hr_attendance = self.env["hr.attendance"]
                biometric_data = self.env["biometric.data"]

                if attendance:
                    for lattendance in attendance:
                        time_att = str(lattendance[2].date()) + ' ' + str(lattendance[2].time())
                        atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                        atten_time = atten_time1 - timedelta(hours=5, minutes=30)
                        atten_time = datetime.strftime(atten_time, '%Y-%m-%d %H:%M:%S')
                        atten_time1 = datetime.strftime(atten_time1, '%Y-%m-%d %H:%M:%S')
                        in_time = datetime.strptime(atten_time1, '%Y-%m-%d %H:%M:%S').time()

                        time_new = str(in_time)
                        time_new = time_new.replace(":", ".", 1)
                        time_new = time_new[0:5]

                        try:
                            del_atten_ids = biometric_data.search([('emp_code', '=', str(lattendance[0])),
                                                                    ('name', '=', atten_time)])
                            if del_atten_ids:
                                continue
                            else:
                                print("Date %s, Name %s: %s" % (lattendance[2].date(), lattendance[2].time(), lattendance[0]))
                                biometric_data.create({'name': atten_time, 'emp_code': lattendance[0], 'mechine_id': record.id})
                        except Exception as e:
                            pass
                            print("Exception..Attendance creation======", e.args)
                zk.enableDevice()
                zk.disconnect()
                return True
            else:
                raise Exception(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))

    @api.model
    def schedule_download(self):
        machines = self.search([])
        for machine in machines:
            try:
                machine.download_attendance()
            except Exception:
                raise Exception(('Warning !'), ("Machine with %s is not connected" % machine.name))

    def clear_attendance(self):
        for record in self:
            machine_ip = record.name
            port = record.port
            zk = zklib.ZKLib(machine_ip, int(port))
            res = zk.connect()
            if res:
                zk.enableDevice()
                zk.disableDevice()
                zk.clearAttendance()
                zk.enableDevice()
                zk.disconnect()
                return True
            else:
                raise Exception(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))


class BiometricData(models.Model):
    _name = "biometric.data"
    _description = "Biometric Data"

    name = fields.Datetime('Date')
    emp_code = fields.Char('Employee Code')
    mechine_id = fields.Many2one('biometric.machine', 'Machine No')
