from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'res.partner'

    sex = fields.Selection(
        selection=[
            ('m', 'male'),
            ('f', 'female'),
        ],
    )
