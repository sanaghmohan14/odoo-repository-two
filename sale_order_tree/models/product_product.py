from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    total_sale_count=fields.Integer(string="Total Sale Count",compute="_compute_total_sale_count")


    def _compute_total_sale_count(self):
        for product in self:
            lines = self.env['sale.order.line'].search([
                ('product_id', '=', product.id)])
            product.total_sale_count = sum(lines.mapped('product_uom_qty'))











