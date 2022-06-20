# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Sale(models.Model):
    """
    A job that runs each day to cancel expired quotations
    """

    _inherit = 'sale.order'

    def _auto_cancel_quotations(self):
        for sale in self.env['sale.order'].search([]).filtered(lambda so:(so.validity_date and so.validity_date < fields.Date.today()) or so.is_expired):
            sale.action_cancel()
