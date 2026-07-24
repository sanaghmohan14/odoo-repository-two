from odoo import models,fields,api
from odoo.release import description


class ProjectProject(models.Model):
    _inherit = "project.task"

    sanagh=fields.Char(string="new")






    @api.onchange('tag_ids')
    def _onchange_tag_ids(self):
        if not self.tag_ids:
            return
        users = self.env['res.users'].search([('skill_types', 'in', self.tag_ids.ids)], limit=1)

        if users:
            self.user_ids=users






    @api.onchange("user_ids")
    def _onchange_user_ids(self):
        self._load_time_lines()


    def _load_time_lines(self):
        x = []
        if not self.user_ids:
            return {
                "warning": {
                    "title": "Warning",
                    "message": "no user to add time sheet"
                }
            }
        for line in self.timesheet_ids:
            x.append(
                fields.Command.create({
                    "user_id": line.user_ids.id,
                })
            )
        self.timesheet_ids = x







    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.state =='done':

            if not rec.effective_hours