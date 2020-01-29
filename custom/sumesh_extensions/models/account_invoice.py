from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sales_code = fields.Char(string='SALES CODE')

