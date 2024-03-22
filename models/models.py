# -*- coding: utf-8 -*-

from odoo import models, fields, api

class State(models.Model):
    _name = 'dh_city.state'
    _description = 'State'

    name = fields.Char(string='State Name', required=True)
    code = fields.Char(string='State Code')
    country_id = fields.Many2one('res.country', string='Country')

class City(models.Model):
    _name = 'dh_city.city'
    _description = 'City'

    name = fields.Char(string='City Name', required=True)
    state_id = fields.Many2one('dh_city.state', string='State')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('dh_city.city', string='City', ondelete='restrict')
    state_id = fields.Many2one('dh_city.state', string='State')

    @api.onchange('city_id')
    def _onchange_city_id(self):
        self.state_id = self.city_id.state_id.id if self.city_id else False

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    city_id = fields.Many2one('dh_city.city', string='City', ondelete='restrict')
    state_id = fields.Many2one('dh_city.state', string='State')

    @api.onchange('city_id')
    def _onchange_city_id(self):
        self.state_id = self.city_id.state_id.id if self.city_id else False
