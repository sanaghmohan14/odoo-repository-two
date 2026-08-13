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


    def action_request_alternate(self):
        self.ensure_one()
        x=[]
        for rec in self:
            print("rec is here")
            if rec.move_raw_ids:
                for i in rec.move_raw_ids:
                    x.append(i.product_id.name)
                    print(x)
                    print("i",i)
                    if i.product_id:
                        print("yes")
                        if i.product_id.qty_available < i.product_uom_qty:
                            print(i.product_id.qty_available)
                            return {
                                "type": "ir.actions.act_window",
                                "name": "alternate",
                                'res_model': 'mrp.wizard',
                                'view_mode': 'form',
                                "target": "new",
                                "context": {
                                    "default_move_id": self.id,
                                    "default_product_id": i.product_id.id,
                                    "default_alternate_product_id":i.product_id.alternate_product_id.id,
                                    # "default_required_qty": self.product_uom_qty,
                                }
                            }







