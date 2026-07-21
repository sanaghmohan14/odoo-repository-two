from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'stock.picking'



    maximum_capacity = fields.Float(string="Maximum Capacity")


    def button_validate(self):
        for i in self:
            if i.picking_type_id.code=="internal":
                location=i.location_dest_id


                current_quantity=sum(self.env['stock.quant'].search([('location_id','=',location.id)]).mapped('quantity'))
                print("current_quantity",current_quantity)

                incoming_quantity=sum(i.move_ids.mapped('product_uom_qty'))
                print("incoming_quantity",incoming_quantity)

                capacity=location.max_capacity
                print("capacity",capacity)

                x=incoming_quantity+current_quantity
                surplus=current_quantity-incoming_quantity
                print("surplus",surplus)

                if x>location.max_capacity:
                    products = " "
                    for j in i.move_ids:
                        products = products + f"{j.product_id.display_name}\n\n"

                        raise ValidationError(
                            f"Maximum capacity reached\n\n\n\n"
                            f"surplus qantity: {surplus}\n\n"
                            f"Products:{products}\n"
                        )
                    # raise ValidationError("exceed maximum capacity")
                else:
                    return super().button_validate()







































