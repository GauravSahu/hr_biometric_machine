# -*- coding: utf-8 -*-

{
    "name": "Biometric Device Integration",
    "version": "1.0",
    "author": "Gaurav Sahu, Randall Castro",
    "category": "Custom",
    "website": "gauravsahu.odoo.com",
    "description": "A Module for Biometric Device Integration",
    "depends": [
        "base",
        "hr"
    ],
    "init_xml": [
    ],
    "data": [
        "views/biometric_machine_view.xml",
        "report/daily_attendance_view.xml",
        "views/schedule.xml",
        "wizard/schedule_wizard.xml",
    ],
    "active": False,
    "installable": True
}
