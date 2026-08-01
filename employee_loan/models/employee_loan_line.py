from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError



class EmployeeLoanLine(models.Model):
    _name="employee.loan.line"
    _description = "fleet service"
    _rec_name = "loan_id"


    loan_id = fields.Many2one('employee.loan',string="Loan")
    date = fields.Date('Date')
    amount = fields.Float('Amount')
    paid = fields.Boolean('Paid Line')