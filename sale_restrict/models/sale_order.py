from odoo import models,fields,api
from odoo.exceptions import ValidationError
from odoo.release import description


class SaleOrder(models.Model):
    _inherit = "sale.order"


    sanagh = fields.Char(string="New Order")



    def action_confirm(self):
        for rec in self:

            if rec.amount_total:

                if rec.amount_total>50000 :
                    if not self.env.user.has_group('sales_team.group_sale_manager'):
                        raise ValidationError("amount exceeded")

            else:
                return super().action_confirm()