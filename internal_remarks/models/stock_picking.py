from odoo import models,fields

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "stock.picking"

    internal_remarks = fields.Text(string="Internal Remarks")