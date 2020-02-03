# -*- coding: utf-8 -*-

from odoo import models, fields


class MovieManagement(models.Model):
    _name = 'movie.management'
    _description = 'movies info'

    name = fields.Char(
        string='Movie Name',
        required=True,
    )
    genre = fields.Selection(
        selection=[
            ('a', 'Comedy'),
            ('b', 'Action'),
            ('c', 'Animated'),
            ('d', 'Horror'),
        ],
    )
    release_year = fields.Integer(
        string='Release Year',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    image = fields.Binary(
        string='Image',
    )
