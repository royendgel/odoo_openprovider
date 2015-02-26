# -*- coding: utf-8 -*-
from openerp import http

# class Openprovider(http.Controller):
#     @http.route('/openprovider/openprovider/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openprovider/openprovider/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openprovider.listing', {
#             'root': '/openprovider/openprovider',
#             'objects': http.request.env['openprovider.openprovider'].search([]),
#         })

#     @http.route('/openprovider/openprovider/objects/<model("openprovider.openprovider"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openprovider.object', {
#             'object': obj
#         })