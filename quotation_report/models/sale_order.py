from odoo import models,fields,api

from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    line_weight = fields.Float(string="line weight", compute="_compute_line_weight")


    @api.depends('product_uom_qty','product_id.weight')
    def _compute_line_weight(self):
        for rec in self:

            print(rec.product_id.weight)
            print(rec.product_uom_qty)

            weight=rec.product_id.weight

            print(weight)

            rec.line_weight=rec.product_uom_qty*weight
            print("weight 1",rec.line_weight)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_weight = fields.Float(string="total weight", compute="_compute_total_weight", store=True)

    @api.depends('order_line.line_weight')
    def _compute_total_weight(self):
        for order in self:
            print(len(order),"length of order")

            order.total_weight = sum(order.order_line.mapped('line_weight'))
            print("total weight",order.total_weight)
