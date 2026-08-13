from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_approved = fields.Boolean(string="Approve")

    alternate_product_id = fields.Many2many('product.template', string="Alternate Product")


