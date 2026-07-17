from datetime import datetime, timedelta
from odoo import fields,models,api



class FleetServiceOrder(models.Model):
    _name="fleet.service.order"
    _description = "fleet service"


    name = fields.Char(string='', readonly=True ,default='New')

    vehicle_id=fields.Many2one('fleet.vehicle',string="Vehicle Model")
    technician_id=fields.Many2one('hr.employee',string="Technician",required=True)
    service_date=fields.Datetime(string="Service Date",default=fields.Date.today())
    state = fields.Selection([('draft','Draft'),('inprogress','Inprogress'),('ready','Ready'),('cancelled','Cancelled'),('done','Done')],string="State",required=True,tracking=True,default="draft")


    # parts_ids=fields.One2many('fleet.service.order.part','order_part_id',string="parts")

    checklist_ids = fields.One2many('fleet.service.order.checklist', 'checklist_id',string="Checklists")

    order_part_ids = fields.One2many('fleet.service.order.part', 'order_part_id',string="Order Parts")

    checklist_id = fields.Many2one('fleet.service.order')
    order_part_id = fields.Many2one('fleet.service.order')



    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.service.order') or 'New'
            return super().create(vals_list)

