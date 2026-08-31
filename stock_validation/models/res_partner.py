from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    block_order=fields.Boolean(string="Block Order")