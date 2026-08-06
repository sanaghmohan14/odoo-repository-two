from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class MachineTools(models.Model):
    _name="machine.tools"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    _rec_name = "machine_uses_id"


    machine_uses_id = fields.Many2one('machine.uses',string="Machines")
    date = fields.Date('Date')
    amount = fields.Float('Amount')
    paid = fields.Boolean('Paid Line')


