{
    'name': "Cinema management",

    'summary': """Cinema management""",

    'description': """
       This module implements cinema management
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'account'],

    # always loaded
    'data': [
        'init_scripts.sql',
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/cinema_report_views.xml',
        'report/timetable_report.xml',
        'report/timetable_report_template.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/movie_views.xml',
        'wizards/sell_ticket_views.xml',
        'views/timetable_views.xml',
        'views/room_views.xml',
        'views/ticket_views.xml',
        'data/mail_templates_data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
