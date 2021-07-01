# -*- coding: utf-8 -*-
# from odoo import http


# class ProdServ(http.Controller):
#     @http.route('/prod_serv/prod_serv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prod_serv/prod_serv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prod_serv.listing', {
#             'root': '/prod_serv/prod_serv',
#             'objects': http.request.env['prod_serv.prod_serv'].search([]),
#         })

#     @http.route('/prod_serv/prod_serv/objects/<model("prod_serv.prod_serv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prod_serv.object', {
#             'object': obj
#         })
