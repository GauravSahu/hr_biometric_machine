# Biometric Device Integration - Odoo

[![Join the chat at https://gitter.im/GauravSahu/hr_biometric_machine](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/GauravSahu/hr_biometric_machine?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/rcastro-tyc/hr_biometric_machine.svg?branch=master)](https://travis-ci.org/rcastro-tyc/hr_biometric_machine)

Step 1:

Install ZKLIB
<pre>
sudo easy_install zklib 
or
sudo pip install zklib
</pre>
Step 2:

Install Module hr_biometric_machine


# Some Usefull Function of ZKLIB

1. To Connect Machine 
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
</pre>
2. To Disconnect Machine
<pre>
zk.disconnect()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	zk.disconnect()
</pre>
3. To Enable  Device
<pre>
zk.enableDevice()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	zk.enableDevice()
</pre>
4. To Disable  Device
<pre>
zk.disableDevice()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	zk.enableDevice()
	zk.disableDevice()
</pre>

5. To Get Device Version
<pre>
zk.version()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
</pre>

6. To Get Device OS Version
<pre>
zk.osversion()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
</pre>

7. To Get Device Name
<pre>
zk.deviceName()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
</pre>

8. To Download Attendance
<pre>
zk.getAttendance()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	print zk.getAttendance()
	zk.enableDevice()
	zk.disconnect()
</pre>

9. To Clear Attendance
<pre>
zk.clearAttendance()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	print zk.clearAttendance()
	zk.enableDevice()
	zk.disconnect()
</pre>

10. To Set User
<pre>
zk.setUser(uid=12345, userid='gauravsahu', name='Gaurav Sahu', password='123456', role=zkconst.LEVEL_ADMIN)
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	print zk.setUser(uid=12345, userid='gauravsahu', name='Gaurav Sahu', password='123456', role=zkconst.LEVEL_ADMIN)
	zk.enableDevice()
	zk.disconnect()
</pre>

11. To Remove Admin User
<pre>
zk.clearAdmin()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	zk.clearAdmin()
	zk.enableDevice()
	zk.disconnect()
</pre>

11. To Get All User
<pre>
zk.getUser()
</pre>
Example:
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	print zk.enableDevice()
	print zk.disableDevice()
	print zk.version()
	print zk.osversion()
	print zk.deviceName()
	zk.getUser()
	zk.enableDevice()
	zk.disconnect()
</pre>


