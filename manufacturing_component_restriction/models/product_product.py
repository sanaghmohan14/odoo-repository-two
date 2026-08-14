from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_approved = fields.Boolean(string="Approve")

    alternate_component_ids = fields.Many2many('product.product',
                                            string="Alternate Product",
                                            relation="product_component_alternate_rel",
                                           column1= "component_id",
                                           column2= "alternate_component_id",
                                            )










