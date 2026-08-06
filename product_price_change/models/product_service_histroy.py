from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class ProductServiceHistory(models.Model):
    _name="product.service.history"
    _rec_name = "product_id"


    product_id = fields.Many2one('product.template')
    previous_price = fields.Float(string="Previous Price")
    new_price = fields.Float(string='New Price')
    changed_by=fields.Many2one('res.users')
    changed_date=fields.Datetime(string='Date of change')
    reason_to_change=fields.Char(string="Reason To Change")
