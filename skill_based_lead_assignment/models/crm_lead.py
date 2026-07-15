from odoo import models,fields,api
from odoo.release import description


class CrmLead(models.Model):
    _inherit = "crm.lead"

    _description = "lead assignment based on tags"

