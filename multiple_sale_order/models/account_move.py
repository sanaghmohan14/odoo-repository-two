
from odoo import models,fields,api
from odoo.release import description


class AccountMove(models.Model):
    _inherit = "account.move"

    _description = "multiple sale order in invoice"

    multiple_sale_order_ids = fields.Many2many('sale.order',string="Multiple Sale Order",domain=[('invoice_status','!=','invoiced')])






    # @api.onchange('multiple_sale_order_ids')
    # def _onchange_multiple_sale_order_ids(self):
    #     if not self.multiple_sale_order_ids:
    #         return
    #     self.invoice_line_ids = [()]
    #     lines=[]
    #     for line in self.multiple_sale_order_ids:
    #         # lines.append(line.id)
    #         # self.invoice_line_ids.extend(lines)





    @api.onchange('multiple_sale_order_ids')
    def _onchange_multiple_sale_order_ids(self):
        """this function is used to add multiple sale order lines in invoice"""

        self.invoice_line_ids = [(fields.Command.clear())]

        new = []
        for i in self.multiple_sale_order_ids:
            for rec in i.order_line:
                new.append(fields.Command.create({
                    'name': rec.name,
                    'product_id': rec.product_id.id,
                    'quantity': rec.product_uom_qty,
                    'price_unit': rec.price_unit,
                }))

        self.invoice_line_ids = new

















