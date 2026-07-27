# hi
# "        meetings = self.env['calendar.event'].search_count([('opportunity_id', '=', rec.id)])
#             # meetings=self.env['calendar.event'].search_count([('opportunity_id','=',rec.id)])"




#project
# @api.onchange('tag_ids')
# def _onchange_tag_ids(self):
#     if not self.tag_ids:
#         return
#     users = self.env['res.users'].search([('skill_types', 'in', self.tag_ids.ids)], limit=1)
#
#     if users:
#         self.user_ids = users




# @api.model_create_multi
# def create(self, vals_list):
#     tasks = super().create(vals_list)
#     for task in tasks:
#         employee = self.env["hr.employee"].search([("skill_type", 'in', task.tag_ids.ids)], limit=1)
#         if employee and employee.user_id:
#             task.user_ids = [(4, employee.user_id.id)]
#     return tasks





# def write(self, vals):
#     print("ok", vals)
#     result = super().write(vals)
#     if "stage_id" in vals:
#         print("yes")
#
#         for task in self:
#             print(task.stage_id.name)
#
#             if task.stage_id.name == "In Progress":
#                 print("inprogress is ok")
#
#                 already = self.env["account.analytic.line"].search([
#                     ('task_id', '=', task.id), ("employee_id", "=", task.user_ids.employee_id.id)], limit=1)
#
#                 print(already)
#
#                 if not already:
#                     self.env['account.analytic.line'].create({
#                         "name": task.name,
#                         "task_id": task.id,
#                         "employee_id": task.user_ids.employee_id.id,
#                         "date": fields.Date.today(),
#                         "unit_amount": 0
#                     })
#     return result
