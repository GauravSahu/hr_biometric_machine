# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime, timedelta
from zklib import zklib


class hr_employee(osv.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"

    _columns = {
        'emp_code': fields.char("Emp Code"),
        'category': fields.char("category"),
    }


class biometric_machine(osv.Model):
    _name= 'biometric.machine'
    _columns = {
        'name': fields.char("Machine IP"),
        'ref_name': fields.char("Location"),
        'port': fields.integer("Port Number"),
        'address_id': fields.many2one("res.partner", 'Working Address'),
        'company_id': fields.many2one("res.company", "Company Name"),
        'atten_ids': fields.one2many('biometric.data', 'mechine_id', 'Attendance')
    }

    def download_attendance(self, cr, uid, ids, context=None):
        machine_ip = self.browse(cr, uid, ids).name
        port = self.browse(cr, uid, ids).port
        zk = zklib.ZKLib(machine_ip, int(port))
        res = zk.connect()
        if res == True:
            zk.enableDevice()
            zk.disableDevice()
            attendance = zk.getAttendance()
            hr_attendance =  self.pool.get("hr.attendance")
            hr_employee = self.pool.get("hr.employee")
            biometric_data = self.pool.get("biometric.data")
            if (attendance):
                for lattendance in attendance:
                    time_att = str(lattendance[2].date()) + ' ' + str(lattendance[2].time())
                    atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                    atten_time = atten_time1 - timedelta(hours=5,minutes=30)
                    atten_time = datetime.strftime(atten_time, '%Y-%m-%d %H:%M:%S')
                    atten_time1 = datetime.strftime(atten_time1, '%Y-%m-%d %H:%M:%S')
                    in_time = datetime.strptime(atten_time1, '%Y-%m-%d %H:%M:%S').time()

                    time_new = str(in_time)
                    time_new = time_new.replace(":", ".", 1)
                    time_new = time_new[0:5]
                    print time_att, lattendance[0]
                    try:
                        del_atten_ids = biometric_data.search(cr, uid, [('emp_code', '=', str(lattendance[0])), ('name', '=', atten_time)])
                        if del_atten_ids:
                            # hr_attendance.unlink(cr, uid, del_atten_ids)
                            continue
                        else:
                            print "Date %s, Name %s: %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0] )
                            a = biometric_data.create(cr, uid, {'name':atten_time, 'emp_code': lattendance[0], 'mechine_id': ids[0]})
                            print a
                    except Exception, e:
                        pass
                        print "exception..Attendance creation======", e.args
            zk.enableDevice()
            zk.disconnect()
            return True
        else:
            raise osv.except_osv(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))

    #Dowload attendence data regularly
    def schedule_download(self, cr, uid, context=None):

            scheduler_line_obj = self.pool.get('biometric.machine')
            scheduler_line_ids = self.pool.get('biometric.machine').search(cr, uid, [])
            for scheduler_line_id in scheduler_line_ids:
                scheduler_line =scheduler_line_obj.browse(cr, uid, scheduler_line_id, context=None)
                try:
                    scheduler_line.download_attendance()
                except:
                    raise osv.except_osv(('Warning !'), ("Machine with %s is not connected" %(scheduler_line.name)))


    def clear_attendance(self, cr, uid, ids, context=None):
        machine_ip = self.browse(cr, uid, ids).name
        port = self.browse(cr, uid, ids).port
        zk = zklib.ZKLib(machine_ip, int(port))
        res = zk.connect()
        if res == True:
            zk.enableDevice()
            zk.disableDevice()
            zk.clearAttendance()
            zk.enableDevice()
            zk.disconnect()
            return True
        else:
            raise osv.except_osv(_('Warning !'), _("Unable to connect, please check the parameters and network connections."))


class biometric_data(osv.osv):
    _name = "biometric.data"
    _columns = {
        'name': fields.datetime('Date'),
        'emp_code': fields.char('Employee Code'),
        'mechine_id': fields.many2one('biometric.machine', 'Mechine No')
    }
