from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'stock.picking'



    maximum_capacity = fields.Float(string="Maximum Capacity")



    def button_validate(self):
        for i in self:
            if i.picking_type_code=="internal":
                location=i.location_dest_id
                print("hi")

                current_quantity=sum(self.env['stock.quant'].search([('location_id','=',location.id),('product_id','=',product.id)]).mapped('quantity'))
                print("current_quantity",current_quantity)

                incoming_quantity=sum(i.move_ids.mapped('quantity'))
                print("incoming_quantity",incoming_quantity)

                x=incoming_quantity+current_quantity

                if x>location.max_capacity:
                    raise ValidationError("exceed maximum capacity")
                else:
                    return super().button_validate()


































