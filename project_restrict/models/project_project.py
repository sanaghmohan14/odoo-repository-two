
from odoo import models,fields,api

from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = "project.task"

    sanagh=fields.Char(string="new")




    # @api.model_create_multi
    # def create(self, vals_list):
    #     tasks = super().create(vals_list)
    #     for task in tasks:
    #         employee = self.env["hr.employee"].search([("skill_type", 'in', task.tag_ids.ids)], limit=1)
    #         if employee and employee.user_id:
    #             task.user_ids = [(4, employee.user_id.id)]
    #     return tasks


    @api.onchange('tag_ids')
    def _onchange_tag_ids(self):
        if not self.tag_ids:
            return
        users = self.env['res.users'].search([('skill_types', 'in', self.tag_ids.ids)], limit=1)

        if users:
            self.user_ids=users





    def write(self,vals):
        result=super().write(vals)
        if "stage_id" in vals:
            for task in self:
                if task.stage_id.name=="In Progress":
                    already=self.env["account.analytic.line"].search([('task_id','=',task.id),("employee_id","=",task.user_ids.employee_id.id)], limit=1)
                    if not already:
                        self.env['account.analytic.line'].create({
                            "name": task.name,
                            "task_id": task.id,
                            "employee_id":task.user_ids.employee_id.id,
                            "date":fields.Date.today(),
                            "unit_amount":0
                        })
        return result





    def write(self,vals):
        result=super().write(vals)
        if "stage_id" in vals:
            for task in self:
                if task.stage_id.name=="Done":
                    total_hours=sum(task.timesheet_ids.mapped("unit_amount"))

                    if total_hours<=0:
                        raise ValidationError("less than zero")
        return result





