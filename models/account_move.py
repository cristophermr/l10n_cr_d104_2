# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class AccountMoveProdServ(models.Model):
    _inherit = "account.move.line"

    x_country_code = fields.Char(related="partner_id.country_id.code", store=True)
    x_account_analytic_plan = fields.Many2one('account.analytic.plan', string="Analytic Plan")

    _logger.info(f"===============================")
    _logger.info(f"DEF14 Pending automatic assignment if it's product or service")
    _logger.info(f"===============================")
    
    '''
    @api.onchange('product_id')
    def prod_serv_update(self):
        result = False
        if self.product_id.type == "service":
            result = self.env['account.analytic.plan'].search([('name','=ilike','Servicios')],limit=1)
        elif self.product_id.type == "product":
            result = self.env['account.analytic.plan'].search([('name','=ilike','Bienes')],limit=1)
        elif self.product_id.type == "consu":
            result = self.env['account.analytic.plan'].search([('name','=ilike','Bienes')],limit=1)
        
        if result == False:
            return
        self.account_analytic_ids = [(6, 0, [result.id] )]
        
        return
    '''