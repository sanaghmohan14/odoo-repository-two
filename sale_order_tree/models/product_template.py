from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"


    def write(self, vals):
        res = super().write(vals)
        if 'list_price' in vals:
            print("list price present")
            for product in self:
                draft_lines=self.env['sale.order.line'].search([('product_id.product_tmpl_id','=',product.id),('order_id.state','=','draft')])

                if draft_lines:
                    print("draft line is present")
                    draft_lines.write(
                        {
                            'price_unit':product.list_price
                        }
                    )