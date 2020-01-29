# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class TicketWizard(models.TransientModel):
    _name = 'ticket.wizard'

    tickets = fields.Integer(
        string='number of tickets to sell',
    )
    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        string='Partner ID',
    )
    product_id = fields.Many2one(
        'product.product',
        required=True,
        string='Product ID',
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        movie_id = self.env.context.get('movie_id')
        movie = self.env['movie.management'].browse(movie_id)
        domain = []
        vals = {}

        products = self.env['product.product'].search([('name', 'ilike', movie.name)])
        domain.extend([('id', 'in', products.ids)])
        vals = {'domain': {'product_id': domain}}
        return vals

    @api.multi
    def confirm(self):
        self.ensure_one()
        timetable_record = self.env['timetable.management'].browse(self._context.get('active_id'))
        if self.tickets <= timetable_record.remaining_seats:
            timetable_record.sold_seats += self.tickets
            invoice = self.env['account.invoice'].create({
                'partner_id': self.partner_id.id,
                'type': 'out_invoice',
                'invoice_line_ids': [(0, 0, {
                    'quantity': self.tickets,
                    'uom_id': self.product_id.uom_id.id,
                    'product_id': self.product_id.id,
                    'name': self.product_id.description_sale or self.product_id.display_name,
                    'price_unit': self.product_id.list_price,
                    'account_id': self.partner_id.property_account_receivable_id.id
                })]
            })
            invoice.action_invoice_open()
            local_context = self.env.context.copy()
            local_context.update({
                'total_amount': invoice.amount_total,
                'invoice_date': invoice.date_invoice
            })
            template_id = self.env.ref('cinema_management.email_template_cinema_management').id
            print(template_id)
            template = self.env['mail.template'].browse(template_id)
            template.with_context(local_context).send_mail(self.id, force_send=True)
            # template_id.send_mail(invoice.id, force_send=True, raise_exception=False, email_values=None, notif_layout=False)
        else:
            raise UserError("Insufficient seats")
