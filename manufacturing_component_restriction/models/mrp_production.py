from odoo import fields,models,api
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'




    # action super to check quantity available or not

    # def action_confirm(self):
    #     print("hiqwert")
    #     for rec in self:
    #         # if rec.move_raw_ids:
    #         for i in rec.move_raw_ids:
    #             print(i.product_id.name)
    #             print(i.product_uom_qty)
    #             if i.product_id:
    #                 if i.product_id.qty_available < i.product_uom_qty:
    #                     print(i.product_id.qty_available)
    #                     return {
    #                         "type": "ir.actions.act_window",
    #                         "name": "alternate",
    #                         'res_model': 'mrp.wizard',
    #                         'view_mode': 'form',
    #                         "target": "new",
    #                         "context": {
    #                             "default_move_id": self.id,
    #                             "default_product_id": i.product_id.id,
    #                             # "default_required_qty": self.product_uom_qty,
    #                         }
    #                     }
    #
    #
    #
    #     return super().action_confirm()


    def action_suggest_alternate(self):
        self.ensure_one()

        unavailable_moves=self.move_raw_ids.filtered(
        lambda move: move.product_id.qty_available < move.product_uom_qty)

        print(unavailable_moves,"moves")

        if not unavailable_moves:
            raise ValidationError("all are in stock")
        if unavailable_moves == 0:
            raise ValidationError("all are in stock")

        if unavailable_moves:
            return {
            "type": "ir.actions.act_window",
            "name": "alternate",
            'res_model': 'mrp.wizard',
            'view_mode': 'form',
            "target": "new",
            "context": {
                "default_order_id":self.id,
                "default_unavailable_component_ids":unavailable_moves.ids,

                }
            }












