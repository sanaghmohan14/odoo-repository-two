from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
from odoo.exceptions import RedirectWarning


class ProductTemplate(models.Model):
    _inherit = "product.template"


    def write(self, vals):
        for rec in self:
            if 'product_id 'in vals:
                print("product present")




