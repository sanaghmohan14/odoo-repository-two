from odoo import fields,models,api
from datetime import datetime, timedelta

class DayWiseAttendances(models.Model):
    _name = 'day.wise.attendances'

    employee_id = fields.Many2one('hr.employee',string='Employee')
    today_date = fields.Date.today()
    date = fields.Datetime(string='Date')
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True, tracking=True, index=True)
    check_out = fields.Datetime(string="Check Out", tracking=True)





    @api.model
    def generate_absentees(self):
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)

        print(today)
        print(tomorrow)

        employees = self.env["hr.employee"].search([('active', '=', True)])
        print(employees)
        for employee in employees:
            present = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id),('check_in', '>=', today),('check_in', '<', tomorrow)])
            print(present)

            if not present:
                self.create({
                    "employee_id": employee.id,
                })


            if present:
                self.env['day.wise.attendance'].unlink({
                    "employee_id":employee.id
                })
