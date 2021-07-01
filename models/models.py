# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class prod_serv(models.Model):
#     _name = 'prod_serv.prod_serv'
#     _description = 'prod_serv.prod_serv'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
