from odoo import models,fields
class SaleOrder(models.Model):
    _inherit = "sale.order"

    _description = "Sale Order Multiple Invoices"

    product_price = fields.Float(string="Price")
