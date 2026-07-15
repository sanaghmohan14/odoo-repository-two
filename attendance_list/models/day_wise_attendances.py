from odoo import fields,models,api
from datetime import datetime, timedelta



class DayWiseAttendances(models.Model):
    _name = 'day.wise.attendances'
    _order = 'date desc'

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

        for employee in employees:

            today_attendance = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id),
                ('check_in', '>=', fields.Datetime.to_datetime(today),),
            ], limit=1)

            if today_attendance:
                continue

            open_attendance = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id),
                ('check_out', '=', False),
                ('check_in', '<', fields.Datetime.to_datetime(today)),
            ], limit=1)

            if open_attendance:
                continue

            exists = self.search([
                ('employee_id', '=', employee.id),
                ('date', '=', today),
            ], limit=1)

            if not exists:
                self.create({
                    'employee_id': employee.id,
                    'date': today,
                })












