from odoo import models,fields
class SaleOrder(models.Model):
    _inherit = "sale.order"

    _description = "Sale Order Multiple Invoices"

    # year=fields.Char(string="Year")
    # multiple_sale_order_ids = fields.Many2oneReference('sale.order', string="Multiple Sale Order",
    #                                            domain=[('invoice_status', '!=', 'invoiced')])
