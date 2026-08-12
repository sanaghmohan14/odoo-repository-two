from odoo import api, fields, models

from odoo.exceptions import ValidationError


class MrpWizard(models.TransientModel):
    _name = 'mrp.wizard'


    first = fields.Many2one('product.product', string="Product")


    def action_confirm(self):
        print("action done")