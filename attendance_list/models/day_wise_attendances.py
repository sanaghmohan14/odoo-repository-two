from odoo import fields,models,api
from datetime import datetime, timedelta



class DayWiseAttendances(models.Model):
    _name = 'day.wise.attendances'
    _order = 'date desc'

    employee_id = fields.Many2one('hr.employee',string='Employee')
    date = fields.Date(string='Date')
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True, tracking=True, index=True)
    check_out = fields.Datetime(string="Check Out", tracking=True)
    # status = fields.Selection({('present',':','present'), ('absent',':','absent')}, string="Status")







    @api.model
    def generate_absentees(self):
        today = fields.Date.today()
        print(today)

        self.search([('date', '=', today)]).unlink()
        employees = self.env['hr.employee'].search([('active', '=', True)])

        print(len(employees))

        for employee in employees:
            today_attendance = self.env['hr.attendance'].search([('employee_id', '=', employee.id),
                ('check_in', '>=', fields.Datetime.to_datetime(today)),
                ('check_in', '<', fields.Datetime.to_datetime(today + timedelta(days=1))),
            ], limit=1)

            print(today_attendance)


            if today_attendance:
                continue

            stayed = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id),
                ('check_out', '=', False),
                ('check_in', '<', fields.Datetime.to_datetime(today)),
            ], limit=1)

            if stayed:
                continue

            self.create({
                'employee_id': employee.id,
                'date': today,
            })




        # @api.model_create_multi
        # def create(self, vals_list):
        #     records = super().create(vals_list)
        #
        #     today = fields.Date.today()
        #
        #     for rec in records:
        #         absentee = self.env['day.wise.attendances'].search([ ('employee_id', '=', rec.employee_id.id),
        #             ('date', '=', today),
        #         ])
        #
        #         absentee.unlink()
        #
        #     return records






