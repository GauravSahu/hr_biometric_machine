from openerp.osv import fields, osv
from datetime import datetime , timedelta
from zklib import zklib
import time
from zklib import zkconst

class biometric_machine(osv.Model):
    _name= 'biometric.machine'
    _columns = {
        'name' : fields.char("Machine IP"),
        'ref_name' : fields.char("Location"),
        'port': fields.integer("Port Number"),
        'address_id' : fields.many2one("res.partner",'Working Address'),
        'company_id': fields.many2one("res.company","Company Name")
    }

    def download_attendance(self, cr, uid, ids, context=None):
        machine_ip = self.browse(cr,uid,ids).name
        port = self.browse(cr,uid,ids).port
        zk = zklib.ZKLib(machine_ip, int(port))
        res = zk.connect()
        if res == True:
            zk.enableDevice()
            zk.disableDevice()
            attendance = zk.getAttendance()
            hr_attendance =  self.pool.get("hr.attendance")
            hr_employee = self.pool.get("hr.employee") 
            if ( attendance ):
                for lattendance in attendance:
                    time_att = str(lattendance[2].date()) + ' ' +str(lattendance[2].time())
                    atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                    atten_time = atten_time1 - timedelta(hours=5,minutes=30)
                    atten_time = datetime.strftime(atten_time,'%Y-%m-%d %H:%M:%S')
                    atten_time1 = datetime.strftime(atten_time1,'%Y-%m-%d %H:%M:%S')
                    in_time = datetime.strptime(atten_time1,'%Y-%m-%d %H:%M:%S').time()
                    employee_id = hr_employee.search(cr,uid,[("emp_code", "=", str(lattendance[0]))])
                    address_id = False
                    category = False
                    if employee_id:
                        address_id = hr_employee.browse(cr,uid,employee_id[0]).address_id
                        category = hr_employee.browse(cr,uid,employee_id[0]).category
                   
                    try:
                        atten_ids = hr_attendance.search(cr,uid,[('employee_id','=',employee_id[0]),('name','=',atten_time)])
                        if atten_ids:
                            continue
                        else:
                            # print "Date %s, Name %s: %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0] )
                            atten_id = hr_attendance.create(cr,uid,{'name':atten_time,'address_id':address_id.id,'category':category,'day':str(lattendance[2].date()),'employee_id':employee_id[0],'action':'sign_in'})
                            # print atten_id
                    except Exception,e:
                        pass
                        # print "Exception..Attendance creation======", e.args
            zk.enableDevice()
            zk.disconnect()
            return True
        else:
            raise osv.except_osv(_('Warning !'),_("Unable to connect, please check the parameters and network connections."))

    def clear_attendance(self, cr, uid, ids, context=None):
        machine_ip = self.browse(cr,uid,ids).name
        port = self.browse(cr,uid,ids).port
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
            raise osv.except_osv(_('Warning !'),_("Unable to connect, please check the parameters and network connections."))


