from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = "stock.move"



    suggested_alternate_id = fields.Many2one('product.product',string="Suggested Alternate Product")

    allowed_alternate_id = fields.Many2many('product.product',
                                           related='product_id.alternate_component_ids',
                                           string="Alternate Product")
