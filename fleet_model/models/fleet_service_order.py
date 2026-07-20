from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError



class FleetServiceOrder(models.Model):
    _name="fleet.service.order"
    _description = "fleet service"


    name = fields.Char(string='', readonly=True ,default='New')

    vehicle_id=fields.Many2one('fleet.vehicle',string="Vehicle Model")
    technician_id=fields.Many2one('hr.employee',string="Technician",required=True)
    service_date=fields.Date(string="Service Date",default=fields.Date.today())
    state = fields.Selection([('draft','Draft'),('confirmed','confirmed'),('inprogress','inprogress'),('done','Done'),('cancelled','Cancelled'),],string="State",required=True,tracking=True,default="draft")


    part_ids = fields.One2many('fleet.service.order.part','order_id',string="parts")

    checklist_ids = fields.One2many('fleet.service.order.checklist', 'order_id',string="Checklists")

    parts_total=fields.Float(string="Total Parts",compute="_compute_parts_total",store=True)
    labor_cost=fields.Float(string="Labor Cost")
    grand_total=fields.Float(string="Grand Total",compute="_compute_grand_total")
    checklist_progress=fields.Float(string="Checklist Progress",compute="_compute_checklist_progress")

    type_ids = fields.Many2many('checklist.type',string="Types")










    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.service.order') or 'New'
            return super().create(vals_list)


    @api.depends('part_ids.quantity','part_ids.unit_price')
    def _compute_parts_total(self):
        for rec in self:
            total=0
            for i in rec.part_ids:
                total=total+i.quantity*i.unit_price
            rec.parts_total=total


    @api.depends('labor_cost','parts_total')
    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total=rec.labor_cost+rec.parts_total



    def action_cancel(self):
        self.state='cancelled'


    @api.depends('checklist_ids.is_done')
    def _compute_checklist_progress(self):
        for rec in self:
            total=len(rec.checklist_ids)
            if total:
                done=len(rec.checklist_ids.filtered('is_done'))
                rec.checklist_progress=(done/total)*100
            else:
                rec.checklist_progress=0

            if rec.checklist_progress==100 and rec.state=='done':
                rec.state='done'



    def action_confrim(self):
        for rec in self:
            if not rec.part_ids:
                raise ValidationError("atleast one part is required")
            rec.state='confirmed'


    def action_start_service(self):
        for rec in self:
            if not rec.technician_id:
                raise ValidationError("Technician  is required")
            rec.state='inprogress'



    def generate_checklist(self):
        for rec in self:
            if rec.checklist_ids:
                raise ValidationError("do not duplicate")

            for checklist in rec.type_ids:
                self.env['fleet.service.order.checklist'].create({
                    'order_id':rec.id,
                    'task_name':checklist.name,

                })

