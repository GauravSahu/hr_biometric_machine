# Biometric Device Integration - Odoo

Step 1:

Install ZKLIB

sudo easy_install zklib 
or
sudo pip install zklib

Step 2:

Install Module Odoo


# Some Usefull Function of ZKLIB

1. To Connect Mechine 

zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()

2. To Disconnect Mechine

zk.disconnect()

Example:
zk = zklib.ZKLib(machine_ip, int(port))
res = zk.connect()
if res == True
	zk.disconnect()

