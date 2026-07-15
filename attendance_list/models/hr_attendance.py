from odoo import models, api, fields

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.model_create_multi
    def create(self, vals_list):
        """used to delete from absentees list when marked present in attendance """
        records = super().create(vals_list)

        today = fields.Date.today()

        for rec in records:
            absentee = self.env['day.wise.attendances'].search([('employee_id', '=', rec.employee_id.id),('date', '=', today), ])

            absentee.unlink()



        return records