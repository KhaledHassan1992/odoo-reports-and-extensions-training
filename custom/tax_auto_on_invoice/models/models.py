# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('tax_line_ids', 'invoice_line_ids')
    def change_acc_id(self):
        for line in self.tax_line_ids:
            if line.account_id.code == '9999':
                if 0.0 <= self.amount_untaxed < 50.0:
                    line.amount = 0
                elif 50.0 <= self.amount_untaxed < 250.0:
                    line.amount = self.amount_untaxed * -0.012
                elif 250.0 <= self.amount_untaxed < 500.0:
                    line.amount = self.amount_untaxed * -0.013
                elif 500.0 <= self.amount_untaxed < 1000.0:
                    line.amount = self.amount_untaxed * -0.014
                elif 1000.0 <= self.amount_untaxed < 5000.0:
                    line.amount = self.amount_untaxed * -0.015
                elif 5000.0 <= self.amount_untaxed <= 10000.0:
                    line.amount = self.amount_untaxed * -0.016
                elif self.amount_untaxed > 10000.0:
                    line.amount = self.amount_untaxed * -0.006
            if line.account_id.code == '8888':
                if 0.0 <= self.amount_untaxed < 50.0:
                    line.amount = 0
                elif 50.0 <= self.amount_untaxed < 250.0:
                    line.amount = self.amount_untaxed * -0.012 * 3
                elif 250.0 <= self.amount_untaxed < 500.0:
                    line.amount = self.amount_untaxed * -0.013 * 3
                elif 500.0 <= self.amount_untaxed < 1000.0:
                    line.amount = self.amount_untaxed * -0.014 * 3
                elif 1000.0 <= self.amount_untaxed < 5000.0:
                    line.amount = self.amount_untaxed * -0.015 * 3
                elif 5000.0 <= self.amount_untaxed <= 10000.0:
                    line.amount = self.amount_untaxed * -0.016 * 3
                elif self.amount_untaxed > 10000.0:
                    line.amount = self.amount_untaxed * -0.006 * 3
            if line.account_id.code == '6666':
                line.amount = self.amount_untaxed * -0.01
            if line.account_id.code == '3333':
                line.amount = self.amount_untaxed * 0.14



class AccountTax(models.Model):
    _inherit = 'account.invoice.tax'

    @api.onchange('invoice_id.amount_untaxed', 'account_id')
    def change_acc_ids(self):
        if self.account_id.code == '9999':
            if self.invoice_id.amount_untaxed < 50.0:
                self.amount = 0
            elif 50.0 <= self.invoice_id.amount_untaxed < 250.0:
                self.amount = self.invoice_id.amount_untaxed * -0.012
            elif 250.0 <= self.invoice_id.amount_untaxed < 500.0:
                self.amount = self.invoice_id.amount_untaxed * -0.013
            elif 500.0 <= self.invoice_id.amount_untaxed < 1000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.014
            elif 1000.0 <= self.invoice_id.amount_untaxed < 5000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.015
            elif 5000.0 <= self.invoice_id.amount_untaxed <= 10000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.016
            elif self.invoice_id.amount_untaxed > 10000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.006
        if self.account_id.code == '8888':
            if self.invoice_id.amount_untaxed < 50.0:
                self.amount = 0
            elif 50.0 <= self.invoice_id.amount_untaxed < 250.0:
                self.amount = self.invoice_id.amount_untaxed * -0.012 * 3
            elif 250.0 <= self.invoice_id.amount_untaxed < 500.0:
                self.amount = self.invoice_id.amount_untaxed * -0.013 * 3
            elif 500.0 <= self.invoice_id.amount_untaxed < 1000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.014 * 3
            elif 1000.0 <= self.invoice_id.amount_untaxed < 5000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.015 * 3
            elif 5000.0 <= self.invoice_id.amount_untaxed <= 10000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.016 * 3
            elif self.invoice_id.amount_untaxed > 10000.0:
                self.amount = self.invoice_id.amount_untaxed * -0.006 * 3
        if self.account_id.code == '7777':
            self.amount = -9
        if self.account_id.code == '6666':
            self.amount = self.invoice_id.amount_untaxed * -0.01
        if self.account_id.code == '5555':
            self.amount = 0
        if self.account_id.code == '4444':
            self.amount = 0
        if self.account_id.code == '3333':
            self.amount = self.invoice_id.amount_untaxed * 0.14


