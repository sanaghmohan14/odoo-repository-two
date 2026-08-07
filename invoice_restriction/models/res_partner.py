from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'





    invoice_hold = fields.Boolean(string="Invoice Hold")
    hold_reason = fields.Text(string="Hold Reason")




