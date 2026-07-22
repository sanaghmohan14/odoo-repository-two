from odoo import models,fields
class SaleOrder(models.Model):
    _inherit = "sale.order"

    _description = "Sale Order Multiple Invoices"

    sanagh = fields.Float(string="Price")
