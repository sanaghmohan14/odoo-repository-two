from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class ProductProduct(models.Model):
    _inherit = "product.template"



    last_price_update = fields.Date(string="Last Update")




    def write(self, vals):
        """used to change the price of product template based on different criteria"""
        if "list_price" in vals:
            new_price = vals["list_price"]
            print(new_price)


            for product in self:
                if  not self.env.user.has_group('sales_team.group_sale_manager'):

                    date_today = fields.Date.today() - timedelta(days=30)
                    print(date_today)

                    sales = self.env['sale.order.line'].search(
                        [('product_id.product_tmpl_id', '=', product.id), ('order_id.date_order', '>=', date_today),
                         ])



                    print(len(sales))

                    if sales:
                        prices = sales.mapped("price_unit")
                        print(prices)

                        average_price = sum(prices) / len(prices)
                        print(average_price)

                        price_80 = average_price * (80/100)
                        print(price_80)

                        if new_price < price_80:
                            raise ValidationError("price is below 80%")
        result = super().write(vals)

        if "list_price" in vals:
            for product in self:
                product.last_price_update = fields.Date.today()
        return result



