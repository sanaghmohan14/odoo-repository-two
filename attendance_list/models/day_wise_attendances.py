from odoo import fields,models,api
from datetime import datetime, timedelta



class DayWiseAttendances(models.Model):
    _name = 'day.wise.attendances'

    employee_id = fields.Many2one('hr.employee',string='Employee')
    date = fields.Datetime(string='Date')
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True, tracking=True, index=True)
    check_out = fields.Datetime(string="Check Out", tracking=True)
    # status = fields.Selection({('present',':','present'), ('absent',':','absent')}, string="Status")





    @api.model
    def generate_absentees(self):
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)
        yesterday = today - timedelta(days=1)

        print(today)
        print(tomorrow)
        print(yesterday)


        employees = self.env["hr.employee"].search([('active', '=', True)])
        print(employees)
        for employee in employees:
            present = self.env['hr.attendance'].search([('employee_id', '=', employee.id),('check_in', '>=', today),('check_in', '<', tomorrow),('check_out', '=', yesterday)], limit=1)
            absent = self.env['day.wise.attendances'].search([('employee_id', '=', employee.id)], limit=1)
            print("c","=",absent)
            if absent and present:
                print("b", "=", absent)
                absent.unlink()
            if not present:
                self.create({
                    "employee_id": employee.id,
                    "date": today,
                    "check_out":yesterday,
                })



