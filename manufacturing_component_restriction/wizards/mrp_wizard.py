from odoo import api, fields, models

from odoo.exceptions import ValidationError


class MrpWizard(models.TransientModel):
    _name = 'mrp.wizard'


    move_id = fields.Many2one('mrp.production',string="Move")

    new_id = fields.Many2one('stock.move',string="New")

    product_id = fields.Many2one('product.product', string="Product" , readonly=True)

    required_qty=fields.Float(string="Required Qty",readonly=True)

    alternate_product_id = fields.Many2one('product.product',
                                           string="Alternate Product")





    def action_replace(self):
        # self.ensure_one()

        print(self.move_id,"move")
        print(self.alternate_product_id,"alternate product")
        print(self.move_id.product_id,"move product")

        for line in self.move_id.move_raw_ids:
            print(len(line))


        self.move_id.move_raw_ids.write({
            "product_id": self.alternate_product_id.id,
        })

        return{
            "type": "ir.actions.client",
            'tag':'reload'
        }