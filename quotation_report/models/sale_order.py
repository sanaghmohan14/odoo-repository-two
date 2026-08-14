from odoo import models,fields,api

from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"


    product_total_price = fields.Float(string="Totall",compute="_compute_weight")

    product_weight = fields.Float(string="Product Weight")



    @api.depends('product_total_price','product_weight')
    def _compute_weight(self):
        for rec in self:
            print(rec.product_weight)
            print(rec.product_uom_qty)
