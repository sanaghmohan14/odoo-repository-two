from odoo import api, fields, models

from odoo.exceptions import ValidationError


class MrpWizard(models.TransientModel):
    _name = 'mrp.wizard'


    move_id = fields.Many2one('stock.move',string="Move")

    product_id = fields.Many2one('product.product', string="Product" , readonly=True)

    required_qty=fields.Float(string="Required Qty")

    alternate_product_id = fields.Many2one('product.product', string="Alternate Product")


    def action_replace(self):
        self.ensure_one()


        self.move_id.write({
            "product_id": self.alternate_product_id.id,
        })

        return{
            "type": "ir.actions.client",
            'tag':'reload'
        }