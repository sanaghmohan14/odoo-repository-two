from datetime import datetime, timedelta
from odoo import fields,models,api



class FleetServiceOrderPart(models.Model):
    _name="fleet.service.order.part"
    _description = "fleet service order part"

    _rec_name = "product_id"




    order_id = fields.Many2one('fleet.service.order',string="Order",required=True)
    product_id = fields.Many2one('product.product',string="Product")
    quantity = fields.Float(string="Quantity",required=True)
    unit_price = fields.Float(string="Unit Price",required=True,)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.unit_price=self.product_id.list_price






