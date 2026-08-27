from odoo import models,fields,api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = "sale.order"




    def create_delivery(self):
        for rec in self:
            if rec.order_line:
                return rec.action_view_delivery()



    # def action_confirm(self):
    #     self.order_line = [(fields.Command.clear())]
    #     self.state = "sale"
    #     # print("hi")


    # def action_confirm(self):
    #     for rec in self:
    #         if rec.order_line:
    #             print("order line is present")
    #             x=len(rec.order_line)
    #             if x<2:
    #                 raise ValidationError("more than 2")
    #         # else:
    #     return super().action_confirm()
    #
    #
    # def action_confrim(self):











