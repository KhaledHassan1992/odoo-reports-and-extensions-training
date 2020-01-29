from odoo import models, fields, api
from datetime import datetime


class SumeshSaleOrder(models.AbstractModel):
    _name = 'report.sumesh_reports.report_sumesh_saleorder'

    line_tax = fields.Integer(string='Taxes Price', compute='_compute_line_tax')

    @api.multi
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        self.counter = 0
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'get_counter': self._get_counter,
            'get_date': self._get_date,
        }

    def _get_counter(self):
        self.counter += 1
        return self.counter

    def _get_date(self):
        self.today_date = datetime.now()
        return "%s.%s.%s" % (self.today_date.day, self.today_date.month, self.today_date.year)

    # def _get_tax(self, obj):
    #     ret = []
    #     taxes = []
    #     for line in obj.order_line:
    #         for account_tax in line.tax_id:
    #             if not account_tax in taxes:
    #                 taxes.append(account_tax)
    #     for account_tax in taxes:
    #         tax = []
    #         ret_amount = 0
    #         lines_amount = 0
    #         for line in obj.order_line:
    #             if account_tax in line.tax_id:
    #                 lines_amount += line.price_subtotal
    #                 amount = (account_tax.amount / 100) * line.price_subtotal
    #                 if amount:
    #                     ret_amount += amount
    #         tax.append(account_tax.name)
    #         tax.append("%.2f" % ret_amount)
    #         ret.append(tax)
    #     return ret