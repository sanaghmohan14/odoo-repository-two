from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class CustomerInvoiceHold(models.Model):
    _name="customer.invoice.hold"
    # _rec_name = "product_id"


    # product_id = fields.Many2one('product.template')

    invoice_hold = fields.Boolean(string="Invoice Hold")
    hold_reason=fields.Text(string="Hold Reason")
    released_by=fields.Many2one('res.users')
    released_date=fields.Datetime(string="Release Date")