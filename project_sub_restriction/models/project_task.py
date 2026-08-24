from odoo import models, fields, api

from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = "project.task"

    def write(self, vals):
        print("ok", vals)
        result = super().write(vals)
        # if not self.env.user.has_group('project.project_stage.manager'):

        for task in self:
            print(task.stage_id.name)
            if task.stage_id.name == "Done":
                if task.child_ids:
                    for rec in task.child_ids:
                        if rec.stage_id.name != "Done":
                            message=task.child_ids.name
                            raise ValidationError("sub task is not completed" f"task: {message}")
                        if not rec.timesheet_ids:
                            raise ValidationError("no time sheet")
            if task.stage_id.name == "Done":
                effective_hours = sum(task.child_ids.mapped('total_hours_spent'))
                # print(task.effective_hours)
                if not task.timesheet_ids:
                    self.env['account.analytic.line'].create({
                        "name": task.name,
                        "task_id": task.id,
                        "unit_amount": effective_hours,

                    })

        return result


        for rec in self:
            rec.total_payable=sum(rec.loan_line_ids.mapped('amount'))