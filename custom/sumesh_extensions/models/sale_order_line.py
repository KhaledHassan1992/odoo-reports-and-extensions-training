from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    """If the states are 'True' then the records are not transferred to the following states
       If the states are 'False' then the records are transferred to the following states """
    optional = fields.Boolean(string='OPT', readonly=True, states={'draft': [('readonly', True)], 'sent': [('readonly', True)]})

    # The below method is used to propagate a field value in Sale Order Line to Account Invoice Line
    @api.multi
    def _prepare_invoice_line(self, qty):
        result = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        result['optional'] = self.optional
        return result
