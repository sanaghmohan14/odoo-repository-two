from odoo import models,fields
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
from odoo.exceptions import RedirectWarning


class ProductTemplate(models.Model):
    _inherit = "product.template"


    alternate_product_id = fields.Many2many('product.product',string="Alternate Product")






