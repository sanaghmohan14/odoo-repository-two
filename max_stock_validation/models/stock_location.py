from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'stock.location'

    max_capacity = fields.Float(string="Maximum Capacity")


    