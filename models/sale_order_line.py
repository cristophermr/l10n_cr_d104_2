# -*- coding: utf-8 -*-

from odoo import models, fields, api

#import logging
#_logger = logging.getLogger(__name__)


class SaleOrderProdServ(models.Model):
    _inherit = "sale.order.line"

    x_country_code = fields.Char(related="order_id.partner_id.country_id.code", store=True)

    @api.onchange('product_template_id')
    def prod_serv_update(self):
        result = False
        
        if self.product_template_id.type == "service":
            result = self.env['account.analytic.tag'].search([('name','=ilike','Servicios')],limit=1)
        elif self.product_template_id.type == "product":
            result = self.env['account.analytic.tag'].search([('name','=ilike','Bienes')],limit=1)
        elif self.product_template_id.type == "consu":
            result = self.env['account.analytic.tag'].search([('name','=ilike','Bienes')],limit=1)
        
        if result == False:
            return

        self.analytic_tag_ids = [(6, 0, [result.id] )]
        
        return
