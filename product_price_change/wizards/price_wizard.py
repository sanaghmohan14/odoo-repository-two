from odoo import api, fields, models,_

from odoo.exceptions import ValidationError


class BulkWizard(models.TransientModel):
    _name = 'price.change.wizard'

    product_id = fields.Many2one('product.template')
    new_price = fields.Float(string="New Price")
    reason_to_change = fields.Char(string="Reason For Change")



    def action_confirm(self):
        self.ensure_one()
        if not self.reason_to_change:
            raise ValidationError("please enter reson for change")
        old_price = self.product_id.list_price
        self.product_id.write(
            {
                "list_price": self.new_price
            }
        )
        self.env["product.service.history"].create(
            {
                "product_id":self.product_id.id,
                "previous_price":old_price,
                "new_price":self.new_price,
                "changed_by":self.env.user.id,
                "reason_to_change":self.reason_to_change,
            }
        )
        return
    {
        "type":"ir.actions.act_window_close"
    }



