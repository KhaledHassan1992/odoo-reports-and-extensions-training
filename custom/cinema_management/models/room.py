# -*- coding: utf-8 -*-

from odoo import models, fields


class RoomManagement(models.Model):
    _name = 'room.management'
    _description = 'room info'

    timetable_ids = fields.One2many(
        'timetable.management',
        'reversed',
    )
    capacity = fields.Integer(
        string='Capacity',
        required=True,
    )
