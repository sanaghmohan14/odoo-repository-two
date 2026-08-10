from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class RevisionTracking(models.Model):
    _name="revision.tracking"
    _rec_name = "sale_id"


    sale_id = fields.Many2one('sale.order')

    sale_order_id = fields.Many2one('sale.order.line')

    revision_number = fields.Integer(string="Revision Number")
    modified_by=fields.Many2one('res.users',string="Revision Owner")
    modified_on=fields.Datetime(string="Revision Date")
    revision_notes=fields.Text(string="Revision Notes")
