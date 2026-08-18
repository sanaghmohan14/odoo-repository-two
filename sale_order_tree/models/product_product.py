from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    total_sale_count=fields.Integer(string="Total Sale Count")











