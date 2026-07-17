from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'stock.picking'


    def max_capacity(self):
        for purchase in self:
            purchase.max_capacity = max(purchase.max_capacity, purchase.max_capacity)


            