from odoo import api, fields, models

from odoo.exceptions import ValidationError


class MrpWizard(models.TransientModel):
    _name = 'mrp.wizard'

    order_id = fields.Many2one('mrp.production', string="Move",required=True)


    unavailable_component_ids = fields.Many2many('stock.move', string="Unavailable Product")



    # def action_replace(self):
    #     for rec in self:
    #         if rec.unavailable_product_line_id:
    #             print("print line is present")
    #
    #             if rec.unavailable_product_id:
    #                 if rec.unavailable_product_id.product_uom_qty> rec.unavailable_product_id.qty_available:
    #                     raise ValidationError("Product not available")
    #
    #     self.ensure_one()
    #     print('asdfasdfasdfasdf')
    #     print('move :::::::', self.move_id)
    #
    #     print(self.move_id, "move")
    #     print(self.alternate_product_id, "alternate product")
    #     print(self.move_id.product_id, "move product")
    #
    #     # for i in self.move_id.move_raw_ids:
    #
    #     self.move_id.move_raw_ids.write({
    #         "product_id": self.alternate_product_id.id,
    #     })
    #
    #     return {
    #         "type": "ir.actions.client",
    #         'tag': 'reload'
    #     }



    def add_component(self):
        self.ensure_one()

        line_to_process=self.unavailable_component_ids.filtered("suggested_alternate_id")
        print(line_to_process,"line to process")

        if not line_to_process:
            raise ValidationError("Product not available")

        unlink_commands=[]
        create_commands=[]

        for move in line_to_process:
            print("move is here")


            self.order_id.write({

                "move_raw_ids":[
                    fields.Command.unlink(move.id),
                    fields.Command.create({
                        'product_id':move.suggested_alternate_id.id,
                        "product_uom_qty": move.product_uom_qty,
                        'product_uom': move.product_uom.id,


                    })
                ]
            })

        return {
                "type":"ir.actions.client",
                "tag":"reload"
            }
