from odoo import fields,models,api

class DayWiseAttendances(models.Model):
    _name = 'day.wise.attendances'

    employee_id = fields.Many2one('res.partner',string='Employee')
    # employee_ids = fields.Many2many('hr.attendance')
    date = fields.Datetime(string='Date')
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True, tracking=True, index=True)
    check_out = fields.Datetime(string="Check Out", tracking=True)

