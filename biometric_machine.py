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