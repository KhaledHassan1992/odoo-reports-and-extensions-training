from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_code = fields.Char(string='SALES CODE', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, default='1X445M')
    ref_name = fields.Char(string='Customer New Reference', compute='_compute_ref_name')

    sale_order_line_count = fields.Integer(string='Sale Order Line Count', compute='_compute_sale_order_line_count')

    # The below method is used to propagate a field value in Sale Order to Account Invoice
    @api.multi
    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        result['sales_code'] = self.sales_code
        return result

    @api.onchange('partner_id')
    def _onchange_customer(self):
        if self.partner_id:
            self.sales_code = self.partner_id.name

    @api.multi
    @api.depends('partner_id', 'client_order_ref')
    def _compute_ref_name(self):
        for record in self:
            if record.client_order_ref:
                record.ref_name = ("[%s] - %s" % (record.client_order_ref, record.partner_id.name))

    @api.multi
    @api.depends('order_line')
    def _compute_sale_order_line_count(self):
        for record in self:
            record.sale_order_line_count = 0
            for line in record.order_line:
                record.sale_order_line_count += len(line)
