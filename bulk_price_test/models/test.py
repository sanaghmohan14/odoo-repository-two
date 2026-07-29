# hi
# "        meetings = self.env['calendar.event'].search_count([('opportunity_id', '=', rec.id)])
#             # meetings=self.env['calendar.event'].search_count([('opportunity_id','=',rec.id)])"
from datetime import timedelta


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





# ("order_id.state", "in", ["sales", "done"])

# product.product_variant_ids.write(
#     {
#         "last_price_update": fields.Date.today(),
#
#     }
# )

# total_hours = sum(task.timesheet_ids.mapped("unit_amount"))


# @api.model
# def _hide_menu(self, debug=False):
#     menus = super()._hide_menus(debug)
#     hidden_menu_ids = self.env.user.menus_ids.ids
#     if hidden_menu_ids:
#         def remove_menu(children):
#             result = []
#             for menu in children:
#                 if menu["id"] not in hidden_menu_ids:
#                     if menu.get("children"):
#                         menu["children"]=remove_menu(menu["children"])
#                         result.append(menu)
#
#             return result
#
#         menus["children"] = remove_menu(menus["children"])
#         return menus



