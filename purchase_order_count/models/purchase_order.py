from odoo import api,fields,models
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    restricted = fields.Boolean(default=False,string="Restricted")
    restricted_count = fields.Integer(string="Restricted Count")
    count = fields.Integer(string="Count")


    def button_confirm(self):
        for rec in self:
            if rec.restricted:
                count_of_order=len(rec.order_line)
                print("count_of_order", count_of_order)
                for line in rec.order_line:
                    if rec.restricted_count<count_of_order:
                        raise ValidationError("Maximum count reached")

            else:
                return super().button_confirm()


    # def action_confirm(self):
    #     for rec in self:
    #         line_count=len(rec.product_line_ids)
    #         for line in rec.product_line_ids:
    #             if line.restricted_count > line.line_count:
    #                 raise ValidationError("consmed qty cannot exceed required qty")
    #             line.consumed_qty = line.required_qty










