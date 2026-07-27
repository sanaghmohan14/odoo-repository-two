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





# total_hours = sum(task.timesheet_ids.mapped("unit_amount"))