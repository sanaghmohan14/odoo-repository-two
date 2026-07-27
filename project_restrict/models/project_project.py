
from odoo import models,fields,api

from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = "project.task"

    sanagh=fields.Char(string="new")





    @api.onchange('tag_ids')
    def _onchange_tag_ids(self):
        """it is used to change the user ids when tag ids is changed"""
        if not self.tag_ids:
            return
        users = self.env['res.users'].search([('skill_types', 'in', self.tag_ids.ids)])
        print(users.mapped("name"))


        if users:
            self.user_ids=users



    def write(self,vals):
        print("ok",vals)
        result=super().write(vals)
        if "stage_id" in vals:
            print("yes")

            for task in self:
                print(task.stage_id.name)

                if task.stage_id.name=="In Progress":
                    print("inprogress is ok")

                    already=self.env["account.analytic.line"].search([
                        ('task_id','=',task.id),("employee_id","=",task.user_ids.employee_id.id)])

                    print(already)

                    user=task.user_ids[:1]

                    if not already:
                        self.env['account.analytic.line'].create({
                            "name": task.name,
                            "task_id": task.id,
                            # "employee_id":task.user_ids.employee_id.id,
                            "user_id": user.id,
                            "employee_id":user.employee_id.id,
                            "date":fields.Date.today(),
                            "unit_amount":0
                        })

                if task.stage_id.name == "Done":
                    print("done is ok")

                    total_hours = sum(task.timesheet_ids.mapped("unit_amount"))
                            # total_hours=sum(task.unit_amount)
                            # if task.unit_amount<=0:

                    if total_hours <= 0:
                        raise ValidationError("less than zero")

        return result










