from datetime import datetime, timedelta
from odoo import fields,models,api



class ChecklistType(models.Model):
    _name="checklist.type"
    _description = "Check list Type"


    name = fields.Char(string='Check list Types')