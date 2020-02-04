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

from odoo.http import route
from odoo.server.addons.portal.controllers.portal import CustomerPortal


class WebsitePortal(CustomerPortal):
    #OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "sex", "company_name"]

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        res = super(WebsitePortal, self).account(redirect=None, **post)
        print(res)
        return res
