# -*- coding: utf-8 -*-
# from odoo import http


# class Openelai(http.Controller):
#     @http.route('/openelai/openelai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openelai/openelai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openelai.listing', {
#             'root': '/openelai/openelai',
#             'objects': http.request.env['openelai.openelai'].search([]),
#         })

#     @http.route('/openelai/openelai/objects/<model("openelai.openelai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openelai.object', {
#             'object': obj
#         })

