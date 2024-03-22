# -*- coding: utf-8 -*-
# from odoo import http


# class DhCityContactCrm(http.Controller):
#     @http.route('/dh_city_contact_crm/dh_city_contact_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_city_contact_crm/dh_city_contact_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_city_contact_crm.listing', {
#             'root': '/dh_city_contact_crm/dh_city_contact_crm',
#             'objects': http.request.env['dh_city_contact_crm.dh_city_contact_crm'].search([]),
#         })

#     @http.route('/dh_city_contact_crm/dh_city_contact_crm/objects/<model("dh_city_contact_crm.dh_city_contact_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_city_contact_crm.object', {
#             'object': obj
#         })
