from datetime import datetime, timedelta
from odoo import fields,models,api



class FleetServiceOrderChecklist(models.Model):
    _name="fleet.service.order.checklist"
    _description = "fleet service order part"

    _rec_name = "checklist_id"



    checklist_id = fields.Many2one('fleet.service.order')

    order_id = fields.Many2one('fleet.service.order',string="Order",required=True)
    product_id=fields.Many2one('product.product',string="Product",required=True)
    is_done = fields.Boolean(string="Is Done",default=False)
    note = fields.Text(string="Note")

    checklist_ids = fields.One2many('fleet.service.order.checklist', 'checklist_id')
