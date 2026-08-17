from odoo import api, fields, models,_

from odoo.exceptions import ValidationError


class MergeWizard(models.TransientModel):
    _name = 'merge.wizard'



    multiple_sale_order_ids = fields.Many2many('sale.order', string="Multiple Sale Order",
                                               relation="sale_order_one_two",
                                               column1="sale_id_one",
                                               column2="sale_one_id_one",
                                               domain=[('state', '==', 'draft')])

    order_line= fields.Many2one ('sale.order.line', string="Order Line",)

    order_id = fields.Many2one('sale.order', string="sale", required=True)





    @api.model_create_multi
    def wizard_merge(self):
        for rec in self:
            # rec.order_line = [(fields.Command.clear())]
            new = []
            for i in self.multiple_sale_order_ids:
                for rec in i.order_line:
                    new.append(fields.Command.create({
                        'name': rec.name,
                        'product_id': rec.product_id.id,
                        'product_uom_qty': rec.product_uom_qty,
                        'price_unit': rec.price_unit,
                    }))
            self.order_line = new


