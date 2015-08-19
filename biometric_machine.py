from openerp.osv import fields, osv
import sys
from datetime import datetime , timedelta
from zklib import zklib
import time
from zklib import zkconst

class biometric_machine(osv.osv):
	_name= "biometric.machine"
	_columns={
		'name' : fields.char("Machine IP"),
		'ref_name' : fields.char("Location"),
		'port': fields.integer("Port Number"),
		'address_id' : fields.many2one("res.partner",'Working Address'),
		'company_id': fields.many2one("res.company","Company Name"),
	}

	def download_attendance(self,cr,uid,ids,context=None):
		
		machine_ip = self.browse(cr,uid,ids).name
		port = self.browse(cr,uid,ids).port
		zk = zklib.ZKLib(machine_ip, int(port))
        print zk
        res = zk.connect()
        print "Connection:", ret

        if res == True:
            print "Enable Device", zk.enableDevice()
            print "Disable Device", zk.disableDevice()

            print "Version:", zk.version()
            print "Version OS:", zk.osversion()
            print "Platform:", zk.platform()
            print "Platform Version:", zk.fmVersion()
            print "Work Code:", zk.workCode()
            print "Work Code:", zk.workCode()
            print "SSR:", zk.ssr()
            print "Pin Width:", zk.pinWidth()
            print "Face Function On:", zk.faceFunctionOn()
            print "Serial Number:", zk.serialNumber()
            print "Device Name:", zk.deviceName()
            attendance = zk.getAttendance()
            print " Get Time:", zk.getTime()

            hr_attendance =  self.pool.get("hr.attendance")
            hr_employee = self.pool.get("hr.employee")

            if ( attendance ):
                for lattendance in attendance:  
                    print "Date %s, Name %s: %s" % ( lattendance[2].date(), lattendance[2].time(), lattendance[0] )
                    time_att = str(lattendance[2].date()) + ' ' +str(lattendance[2].time())

                    atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
                    atten_time = atten_time1 - timedelta(hours=5,minutes=30)
                    atten_time = datetime.strftime(atten_time,'%Y-%m-%d %H:%M:%S')
                    atten_time1 = datetime.strftime(atten_time1,'%Y-%m-%d %H:%M:%S')
                    in_time = datetime.strptime(atten_time1,'%Y-%m-%d %H:%M:%S').time()
                    employee_id = hr_employee.search(cr,uid,[("emp_code", "=", str(lattendance[0]))])
                    time_new = str(in_time)
                    time_new = time_new.replace(":",".",1)
                    time_new = time_new[0:5]
                    print time_att,lattendance[0],employee_id
                    try:
                        del_atten_ids = hr_attendance.search(cr,uid,[('employee_id','=',employee_id[0]),('name','=',atten_time)])
                        if del_atten_ids:
                            hr_attendance.unlink(cr,uid,del_atten_ids)
                        a = hr_attendance.create(cr,uid,{'name':atten_time,'address_id':address_id.id,'category':category,'in_time':str(time_new),'name1':atten_time,'day':str(lattendance[2].date()),'employee_id':employee_id[0],'action':'sign_in'})
                        print a
                    except Exception,e:
                        pass
                        print "exception..Attendance creation======", e.args
            
            print "Get Time:", zk.getTime()
            print "Enable Device", zk.enableDevice()
            print "Disconnect:", zk.disconnect() 
        