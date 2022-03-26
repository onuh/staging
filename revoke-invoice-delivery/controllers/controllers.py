# -*- coding: utf-8 -*-
# from odoo import http


# class Tradedepot-technical-test(http.Controller):
#     @http.route('/tradedepot-technical-test/tradedepot-technical-test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tradedepot-technical-test/tradedepot-technical-test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tradedepot-technical-test.listing', {
#             'root': '/tradedepot-technical-test/tradedepot-technical-test',
#             'objects': http.request.env['tradedepot-technical-test.tradedepot-technical-test'].search([]),
#         })

#     @http.route('/tradedepot-technical-test/tradedepot-technical-test/objects/<model("tradedepot-technical-test.tradedepot-technical-test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tradedepot-technical-test.object', {
#             'object': obj
#         })
