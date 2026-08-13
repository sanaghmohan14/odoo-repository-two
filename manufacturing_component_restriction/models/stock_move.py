from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = "stock.move"




    def action_request_alternate(self):

        self.ensure_one()

        if self.product_id.qty_available>=self.product_uom_qty:
            raise ValidationError("Product Product Already Available")

        return {
            "type": "ir.actions.act_window",
            "name":"alternate",
            'res_model': 'mrp.wizard',
            'view_mode': 'form',
            "target": "new",
            "context": {
                "default_move_id":self.id,
                "default_product_id":self.product_id.id,
                "default_required_qty":self.product_uom_qty,
            }
        }

