from odoo import models,fields,api
from odoo.release import description


class CrmLead(models.Model):
    _inherit = "res.users"


    _description = "lead assignment based on tags"

    tag_ids = fields.Many2many('crm.tag', string="Tags", )

    xx=fields.Integer(string="X")
    yy=fields.Integer(string="Y")
