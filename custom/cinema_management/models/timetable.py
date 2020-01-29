# -*- coding: utf-8 -*-

import base64

from odoo import models, fields, api


class TimetableManagement(models.Model):
    _name = 'timetable.management'
    _description = 'timetable info'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Datetime(
        string='Date',
        required=True,
    )
    movie = fields.Many2one(
        'movie.management',
        ondelete='set null',
        string='Movie',
        required=True,
    )
    reversed = fields.Many2one(
        'room.management',
    )
    premier = fields.Boolean(
        string='Premier',
    )

    total_seats = fields.Integer(
        string='Total Seats',
        compute='_compute_total_seats',
        store=True,
    )
    sold_seats = fields.Integer(
        String='Sold Seats',
        track_visibility=True,
    )
    remaining_seats = fields.Integer(
        string='Remaining Seats',
        compute='_compute_remaining_seats',
        track_visibility=True,
        store=True,
    )

    @api.depends('reversed', 'reversed.capacity')
    def _compute_total_seats(self):
        for record in self:
            record.total_seats = record.reversed.capacity

    @api.depends('total_seats', 'sold_seats')
    def _compute_remaining_seats(self):
        for record in self:
            record.remaining_seats = record.total_seats - record.sold_seats

    @api.multi
    def print_timetable(self):
        self.ensure_one()
        pdf = self.env.ref('cinema_management.timetable_report').render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(pdf[0])
        name = "Timetable Report"
        return self.env['ir.attachment'].create({
            'name': name,
            'type': 'binary',
            'datas': b64_pdf,
            'datas_fname': name + '.pdf',
            'store_fname': name,
            'res_model': self._name,
            'res_id': self.id
        })
