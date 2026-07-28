from odoo import api, fields, models



class ResUsers(models.Model):
    _inherit = 'res.users'

    menus_ids = fields.Many2many('ir.ui.menu')






