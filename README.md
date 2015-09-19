# Biometric Device Integration - Odoo

Step 1:

Install ZKLIB
<pre>
sudo easy_install zklib 
or
sudo pip install zklib
</pre>
Step 2:

Install Module Odoo


# Some Usefull Function of ZKLIB

1. To Connect Mechine 
<pre>
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
</pre>
2. To Disconnect Mechine
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

