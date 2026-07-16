from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'



    partner_id=fields.Many2one('res.partner')


