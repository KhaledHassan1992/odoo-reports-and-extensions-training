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
    "name": "Sumesh Extension",
    "summary": "Sumesh Extension",
    "description": """
       Sumesh Extension description
    """,
    "version": "12.0.1.0.0",
    "category": "Uncategorized",
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
        "views/sale_order_view.xml",
        "views/account_invoice_view.xml",
        "views/sale_order_line_view.xml",
        "views/account_invoice_line_view.xml",
        "views/res_partner_view.xml",
        "reports/sale_report_templates_inherit.xml",
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
