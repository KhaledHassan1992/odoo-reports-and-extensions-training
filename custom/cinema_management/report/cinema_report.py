# -*- coding: utf-8 -*-

from odoo import tools
from odoo import api, fields, models


class CinemaReport(models.Model):
    _name = "cinema.report"
    _auto = False
    _description = "Sales Analysis Report"

    name = fields.Char(
        string='Movie Name',
        readonly=True,
    )
    genre = fields.Selection(
        selection=[('a', 'Comedy'), ('b', 'Action'), ('c', 'Animated'), ('d', 'Horror')],
        readonly=True,
    )
    release_year = fields.Integer(
        string='Release Year',
        readonly=True,
    )

    date = fields.Datetime(
        string='Date',
        readonly=True,
    )
    movie = fields.Many2one(
        'movie.management',
        string='Movie',
        readonly=True,
    )
    # reversed = fields.Many2one('room.management', string='Reversed', readonly=True)
    premier = fields.Boolean(
        string='Premier',
        readonly=True,
    )
    total_seats = fields.Integer(
        string='Total Seats',
        readonly=True,
    )
    sold_seats = fields.Integer(
        String='Sold Seats',
    )
    remaining_seats = fields.Integer(
        string='Remaining Seats',
        readonly=True,
    )

    capacity = fields.Integer(
        string='Capacity',
        readonly=True,
    )

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = """
                create or replace view %s as (
                    select
                        mm.name as name,
                        mm.genre as genre,
                        mm.release_year as release_year,
                        tm.id as id,
                        tm.date as date,
                        tm.movie as movie,
                        tm.premier as premier,
                        tm.total_seats as total_seats,
                        tm.sold_seats as sold_seats,
                        tm.remaining_seats as remaining_seats,
                        rm.capacity as capacity
                    from timetable_management as tm
                    full outer join room_management as rm on (tm.reversed = rm.id)
                    join movie_management as mm on (tm.movie = mm.id));  
            """ % self._table
        self.env.cr.execute(query)
