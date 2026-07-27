from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class ProductProduct(models.Model):
    _inherit = "product.template"



    last_price_update = fields.Date(string="Last Update")





    def write(self, vals):
        if "list_price" in vals:
            new_price = vals["list_price"]
            print(new_price)
            if  self.env.user.has_group('sales_team.group_sale_manager'):
                date_today = fields.Date.today()-timedelta(days=30)
                print(date_today)
                sales=self.env['sale.order.line'].search([('product_id.product_tmpl_id','=','product_id'),('order_id.date_order','>=',date_today)])
                print(len(sales))

























