# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class configure_attendence(osv.osv_memory):

    _name = "configure.attendence"
    _columns = {
        'interval_number': fields.integer(string="Interval Number"),
        'interval_type': fields.selection([('minutes', 'Minutes'), ('hours', 'Hours'), ('work_days', 'Work Days'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], string = "Interval Unit"),
    }

    def _get_interval_number(self, cr, uid, context):
        line_id = self.pool.get('ir.cron').search(cr, uid, [('name', 'ilike', 'Download Attendence')])
        return self.pool.get('ir.cron').browse(cr, uid, line_id).interval_number

    def _get_interval_type(self, cr, uid, context):
        line_id = self.pool.get('ir.cron').search(cr, uid, [('name', 'ilike', 'Download Attendence')])
        return self.pool.get('ir.cron').browse(cr, uid, line_id).interval_type


    _defaults = {
        'interval_number': _get_interval_number,
        'interval_type': _get_interval_type
    }

    def update_interval(self, cr, uid, ids, context):
 
        for line in self.browse(cr, uid, ids):
            interval_number = line.interval_number
            interval_type = line.interval_type

        line_id = self.pool.get('ir.cron').search(cr, uid, [('name', 'ilike', 'Download Attendence')])
        schedule_obj = self.pool.get('ir.cron').browse(cr, uid, line_id)
        schedule_obj.write({'interval_number': interval_number, 'interval_type': interval_type})

configure_attendence()