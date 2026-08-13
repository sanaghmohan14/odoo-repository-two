from odoo import fields,models,api
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'









    # action super to check quantity available or not

    # def action_confirm(self):
    #     print("hiqwert")
    #     for rec in self:
    #         if rec.move_raw_ids:
    #             for i in rec.move_raw_ids:
    #                 print(i.product_id.name)
    #                 print(i.product_uom_qty)
    #                 if i.product_id:
    #                         if i.product_id.qty_available < i.product_uom_qty:
    #                             print(i.product_id.qty_available)
    #                             raise ValidationError("not enough qty")
    #
    #                             # if i.product_id.product_uom_qty > i.qty_available:
    #                             #     raise ValidationError(" there is no enough quanity")
    #
    #
    #         else:
    #             print("done")
    #     return super().action_confirm()
    #


    # def action_alternate(self):
    #     print("hi")

    def action_request_alternate(self):

        self.ensure_one()

        if self.product_id.qty_available >= self.product_uom_qty:
            raise ValidationError("Product Product Already Available")

        return {
            "type": "ir.actions.act_window",
            "name": "alternate",
            'res_model': 'mrp.wizard',
            'view_mode': 'form',
            "target": "new",
            "context": {
                "default_move_id": self.id,
                "default_product_id": self.product_id.id,
                "default_required_qty": self.product_uom_qty,
            }
        }










