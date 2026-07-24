from odoo import models,fields,api
from odoo.release import description


class HrEmployee(models.Model):
    _inherit = "hr.employee"



    skill = fields.Selection([('design','design'),('backend','backend')],string="Skill")

    skill_types = fields.Many2many('project.tags',string="Project skills")

