from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError



class MachineUses(models.Model):
    _name="machine.uses"

    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='', readonly=True ,default='New')
    employee_id=fields.Many2one('hr.employee',string="Employee",reqired=True)
    machine_name=fields.Char(string="Machine Name",required=True)
    machine_use=fields.Char(string="Machine Use",required=True)
    start_date=fields.Datetime(string="Start Date")
    state = fields.Selection(
        [('draft', 'Draft'), ('approved', 'approved'), ('ongoing', 'ongoing'), ('paid', 'paid'),
         ('cancelled', 'Cancelled'), ], string="State", required=True, tracking=True, default="draft")

    machine_tools_ids = fields.One2many('machine.tools', 'machine_uses_id')


    machine_amount = fields.Integer(string="Amount",required=True)

    installment_count = fields.Integer(string="Installment Count",default=1)

    installment_amount = fields.Integer(string="Installment Amount",store=True)

    total_payable = fields.Integer(string="Total Payable",compute='_compute_total_payable',store=True)

    machine_history = fields.Char()
    tools_count = fields.Integer(string="Tool Count",compute='compute_tools_count')

    amount = fields.Float(string="Loan Amount")
    installment_date = fields.Datetime(string="Installment Date")

    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('machine.uses') or 'New'
            return super().create(vals_list)

    @api.onchange('machine_amount','installment_count')
    def _onchange_grand_total(self):
        """used to  compute the grand total based on labor cost and parts total"""
        for rec in self:
            rec.installment_amount=rec.machine_amount/rec.installment_count


    @api.depends('machine_tools_ids.amount')
    def _compute_total_payable(self):
        """calculate the total amount of labor charge"""
        for rec in self:
            rec.total_payable=sum(rec.machine_tools_ids.mapped('amount'))


    def action_view_machine_tools(self):
        print("hi")

    def compute_tools_count(self):
        for rec in self:
            rec.tools_count = len(rec.machine_tools_ids)


    def action_view_machines(self):
        print("hi")
        return {
            "type": "ir.actions.act_window",
            "name": "loans",
            "res_model": "machine.tools",
            "view_mode": "list,form",
            "domain": [("machine_uses_id", "=", self.id)],

        }



    def action_create_installment(self):
        for rec in self:
            rec.amount = rec.total_payable / rec.installment_count
            rec.installment_date = rec.start_date
            for i in range(rec.installment_count):
                self.env['machine.tools'].create(
                    {
                        'machine_uses_id': rec.id,
                        'date': 'installment_date',
                        'amount': 'amount'
                    }
                )