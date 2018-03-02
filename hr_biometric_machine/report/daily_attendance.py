
# -*- coding: utf-8 -*-

from openerp import tools
from openerp.osv import fields, osv


class report_daily_attendance(osv.osv):
    _name = "report.daily.attendance"
    _auto = False

    _columns = {
        'name': fields.many2one('hr.employee', 'Employee'),
        'day': fields.date('Date'),
        'address_id': fields.many2one('res.partner', 'Working Address'),
        'category': fields.char('category'),
        'punch': fields.integer('Number of Punch'),
        'in_punch': fields.datetime('In Punch'),
        'out_punch': fields.datetime('Out Punch'),
    }
    _order = 'day desc'
    def init(self, cr):
        tools.drop_view_if_exists(cr, 'report_daily_attendance')
        cr.execute("""
            create or replace view report_daily_attendance as (
                select
                    min(id) as id,
                    employee_id as name,
                    Count(day) as punch,
                    day as day,
                    address_id as address_id,
                    category as category,
                    min(name) as in_punch ,
                    case when min(name) != max(name) then max(name)  end as out_punch
                from
                    hr_attendance
                GROUP BY
                    employee_id,day,address_id,category

            )
        """)
report_daily_attendance()
