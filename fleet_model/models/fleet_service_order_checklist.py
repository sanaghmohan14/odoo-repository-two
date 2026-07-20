from datetime import datetime, timedelta
from odoo import fields,models,api



class FleetServiceOrderChecklist(models.Model):
    _name="fleet.service.order.checklist"
    
    _description = "fleet service order part"

    _rec_name = "task_name"



    order_id = fields.Many2one('fleet.service.order',string="Order",required=True)
    task_name=fields.Char(string="Task Name")
    is_done = fields.Boolean(string="Is Done",default=False)
    note = fields.Text(string="Note")

