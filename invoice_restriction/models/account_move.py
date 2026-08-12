from openpyxl.worksheet import related

from odoo.exceptions import ValidationError

from odoo import models,fields,api
from odoo.release import description


class AccountMove(models.Model):
    _inherit = "account.move"

    _description = "multiple sale order in invoice"


    customer_invoice_hold= fields.Boolean(related="partner_id.invoice_hold",string="Invoice Hold")



    def action_post(self):
        for rec in self:
            x=self.partner_id.name
            print(x)
            # if not self.env.user.has_group('sales_team.group_sale_manager'):
            if rec.partner_id.invoice_hold:
                raise ValidationError("invoice on hold")
        return super().action_post()



    def action_remove(self):
        if self.env.user.has_group('sales_team.group_sale_manager'):
            for rec in self:
                if rec.partner_id.invoice_hold:
                    rec.partner_id.write({
                        'invoice_hold': False,
                    })

                    rec.action_post()
            return True


        else:
            raise ValidationError("You are not allowed to perform this action")


