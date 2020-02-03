# -*- coding: utf-8 -*-

from odoo import models, fields


class TicketManagement(models.Model):
    _inherit = 'product.product'

    e_ticket = fields.Boolean(
        string='e_Ticket',
    )
