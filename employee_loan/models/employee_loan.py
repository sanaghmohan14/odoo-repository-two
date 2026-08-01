from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class EmployeeLoan(models.Model):
    _name="employee.loan"

    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='', readonly=True ,default='New')
    employee_id=fields.Many2one('hr.employee',string="Employee")
    loan_amount=fields.Integer(string="Loan Amount")
    installment_count=fields.Integer(string="Installment Count",default=1)
    start_date=fields.Datetime(string="Start Date")
    state = fields.Selection(
        [('draft', 'Draft'), ('approved', 'approved'), ('ongoing', 'ongoing'), ('paid', 'paid'),
         ('cancelled', 'Cancelled'), ], string="State", required=True, tracking=True, default="draft")

    loan_line_ids = fields.One2many('employee.loan.line', 'loan_id')


    installment_amount = fields.Integer(string="Installment Amount",store=True)
    total_payable = fields.Float(string="Total Payable" ,compute='labor_total')

    loan_counts = fields.Integer(string="Loan Counts", compute='compute_loan_count')

    employee_loan_history = fields.Char(action="action_view_material")



    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('employee.loan') or 'New'
            return super().create(vals_list)




    #
    # @api.depends('loan_amount','installment_count')
    # def _compute_grand_total(self):
    #     """used to  compute the grand total based on labor cost and parts total"""
    #     for rec in self:
    #         rec.installment_amount=rec.loan_amount/rec.installment_count


    @api.onchange('loan_amount','installment_count')
    def _onchange_grand_total(self):
        """used to  compute the grand total based on labor cost and parts total"""
        for rec in self:
            rec.installment_amount=rec.loan_amount/rec.installment_count











    #
    # @api.onchange('loan_amount')
    # def _onchange_loan_amount(self):
    #     for rec in self:
    #         if rec.loan_amount:
    #             rec.total_payable = rec.loan_amount



    @api.depends('loan_line_ids.amount')
    def labor_total(self):
        """calculate the total amount of labor charge"""
        for rec in self:
            rec.total_payable=sum(rec.loan_line_ids.mapped('amount'))


    def action_approve_loan(self):
        for rec in self:
            if rec.loan_amount>0:
                rec.state='approved'
            else:
                raise ValidationError("loan amount must be greater than 0")


    def compute_loan_count(self):
        for rec in self:
            rec.loan_counts = len(rec.loan_line_ids)



    def action_view_material(self):
        print("hi")
        return {
            "type": "ir.actions.act_window",
            "name": "loans",
            "res_model": "employee.loan.line",
            "view_mode": "list,form",
            "domain": [("loan_id", "=", self.id)],

        }


    # def action_create_installment(self):
    #     for rec in self:
    #













    #
    #
    # @api.depends('loan_amount','installment_count')
    # def sum_of_cost(self):
    #     """calculate sum of the amount labor charge + product charge"""
    #     for rec in self:
    #         rec.total_sum=rec.labor_total_amount+rec.total+rec.estimated_amount

