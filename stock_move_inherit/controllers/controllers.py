# -*- coding: utf-8 -*-
# from odoo import http


# class StockMoveInherit(http.Controller):
#     @http.route('/stock_move_inherit/stock_move_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_move_inherit/stock_move_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_move_inherit.listing', {
#             'root': '/stock_move_inherit/stock_move_inherit',
#             'objects': http.request.env['stock_move_inherit.stock_move_inherit'].search([]),
#         })

#     @http.route('/stock_move_inherit/stock_move_inherit/objects/<model("stock_move_inherit.stock_move_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_move_inherit.object', {
#             'object': obj
#         })
