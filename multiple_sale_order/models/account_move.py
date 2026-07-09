from odoo import models,fields
class SaleOrder(models.Model):
    _inherit = "account.move"

    _description = "multiple sale order in invoice"

    multiple_sale_order_ids = fields.Many2many('sale.order',string="Multiple Sale Order")