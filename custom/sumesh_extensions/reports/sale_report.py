from odoo import models, fields, api


class SaleOrderReport(models.AbstractModel):
    _name = 'report.sale.report_saleorder'

    @api.multi
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        self.counter = 0
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'get_counter': self._get_counter
        }

    def _get_counter(self):
        self.counter += 1
        return self.counter
