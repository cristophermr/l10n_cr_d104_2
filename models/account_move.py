# -*- coding: utf-8 -*-

from odoo import models, fields, api

#import logging
#_logger = logging.getLogger(__name__)

class AccountMoveProdServ(models.Model):
    _inherit = "account.move.line"

    x_country_code = fields.Char(related="partner_id.country_id.code", store=True)

    x_prod_serv = fields.Selection([
        ('b', 'Bien'),
        ('s', 'Servicio'),
    ], string="Bien/Servicio")

    @api.onchange('product_id')
    def prod_serv_update(self):

        if self.product_id.type == "service":
            self.x_prod_serv = 's'
        elif self.product_id.type == "product":
            self.x_prod_serv = 'b'
        elif self.product_id.type == "consu":
            self.x_prod_serv = 'b'

        return
