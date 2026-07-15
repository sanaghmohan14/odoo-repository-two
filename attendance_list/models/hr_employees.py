# from odoo import models,fields,api
# from odoo.release import description
#
#
# class HrEmployee(models.Model):
#     # _inherit = "hr.employee"

#
#         if present:
#             if absent:
#                 absent.unlink()
#         else:
#             if not absent:
#                 self.create({
#                     'employee_id': employee.id,
#                     'date': today,
#                 })
#


# @api.model
# def generate_absentees(self):
#     today = fields.Date.today()
#     tomorrow = today + timedelta(days=1)
#
#     print(today)
#     print(tomorrow)
#
#     employees = self.env["hr.employee"].search([('active', '=', True)])
#     print(employees)
#     for employee in employees:
#         present = self.env['hr.attendance'].search([
#             ('employee_id', '=', employee.id),('check_in', '>=', today),('check_in', '<', tomorrow)])
#         print(present)
#
#         if not present:
#             self.create({
#                 "employee_id": employee.id,
#             })
#
#         absent = self.env['day.wise.attendances'].search([('employee_id', '=', employee.id),('date','=',today)])
#
#         if absent:
#             absent.unlink()


    # from odoo import models, api, fields
    #
    # class HrAttendance(models.Model):
    #     _inherit = 'hr.attendance'
    #
    #     @api.model_create_multi
    #     def create(self, vals_list):
    #         records = super().create(vals_list)
    #
    #         for attendance in records:
    #             self.env['day.wise.attendances'].search([
    #             ('employee_id', '=', attendance.employee_id.id),
    #             ('date', '=', fields.Date.to_date(attendance.check_in)),
    #         ]).unlink()
    #
    #         return records


# employees = self.env["hr.employee"].search([('active', '=', True)])
# print(employees)
# for employee in employees:
#     present = self.env['hr.attendance'].search([('employee_id', '=', employee.id),('check_in', '>=', today),('check_in', '<', tomorrow),('check_out', '<', today)], limit=1)
#     absent = self.env['day.wise.attendances'].search([('employee_id', '=', employee.id)], limit=1)
#     print("c","=",absent)
#     if absent and present:
#         print("b", "=", absent)
#         absent.unlink()
#     if not present:
#         self.create({
#             "employee_id": employee.id,
#             "date": today,
#             "check_out":yesterday,
#         })


    # @api.model_create_multi
    # def create(self,vals_list):
    #     records=super().create(vals_list)
    #
    #     today=fields.Date.today()
    #
    #     for employee in employees:
    #         absentee=self.env['day.wise.attendance'].search([('employee_id','=',employee.id),('date','=',today)])
    #
    #         absentee.unlink()
    #     return records


    #
    #
    # def create_attendances(self):
    #     today=fields.Date.today()
    #     print(today)
    #     self.search(['date','=',today]).unlink()
    #
    #     employee=self.env['hr.employee'].search([('employee_id','=',employee.id),('active','=',True)])










