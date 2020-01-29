# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2019 Openfellas (http://openfellas.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract support@openfellas.com
#
##############################################################################
{
    "name": "Sumesh Reports",
        "summary": "Sumesh Reports",
    "description": """
       Sumesh custom reports
    """,
    "version": "12.0.1.0.0",
    "category": "Reports",
    "website": "https://openfellas.com/",
    "author": "openfellas",
    "depends": [
        "base", "sale",
    ],
    "data": [
        # "security/model_name_security.xml",
        # "security/ir.model.access.csv",
        # "templates/assets.xml",
        # "views/report_name.xml",
        # "views/model_name_view.xml",
        "sumesh_reports.xml",
        "reports/layouts.xml",
        "reports/sale_order_report.xml",
        # "wizards/wizard_model_view.xml",
    ],
    "demo": [
        # "demo/module_name.xml",
    ],
    "qweb": [
        # "static/src/xml/module_name.xml",
    ],
    "application": False,
    "installable": True,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    # "post_load": "post_load",
    # "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
}
