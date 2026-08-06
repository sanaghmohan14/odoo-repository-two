from odoo import api, fields, models,_

from odoo.exceptions import ValidationError


class BulkWizard(models.TransientModel):
    _name = 'price.change.wizard'

    reason_to_change = fields.Char(string="Reason For Change")



    def action_product_history(self):
        print("hi action")

