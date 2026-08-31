from odoo import models,fields,api
from odoo.exceptions import ValidationError
from odoo.release import description



class SaleOrder(models.Model):
    _inherit = "stock.picking"



    def action_confirm(self):
        print("hi")
        for rec in self:
            print(rec)
            if rec.partner_id.block_order:
                raise ValidationError("order is blocked")
            else:
                print("order is not blocked")

        return super().action_confirm()