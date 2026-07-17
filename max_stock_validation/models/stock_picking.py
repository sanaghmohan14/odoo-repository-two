from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'stock.picking'



    max_capacity = fields.Float(string="Maximum Capacity")


    # def capacity(self):
    #     for i in self:
    #         if i.picking_type_id == 'internal':
































