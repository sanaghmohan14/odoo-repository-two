from odoo import fields,models,api
from odoo.exceptions import ValidationError



class MrpProduction(models.Model):
    _name="mrp.production.ext"
    _description = "mrp production"


    name = fields.Char(string='', readonly=True ,default='New')
    product_id = fields.Many2one('product.product',required=True)
    bom_id = fields.Many2one('mrp.bom',required=True)
    quantity = fields.Float(required=True)
    planned_date = fields.Date(required=True)
    state = fields.Selection([('draft','Draft'),('confirmed','confirmed'),('inprogress','inprogress'),('done','Done'),('cancelled','Cancelled'),],string="State",required=True,tracking=True,default="draft")
    material_line_ids = fields.One2many('mrp.production.material','production_id',string="Materials")




    #
    # @api.model
    # def create(self, vals_list):
    #     """create function is used to create the reference/ sequence id when creating a  new repair service """
    #     for vals in vals_list:
    #         if vals.get('name', 'New') == 'New':
    #             vals['name'] = self.env['ir.sequence'].next_by_code('mrp.production.ext') or 'New'
    #         return super().create(vals_list)
    #
    #
    # @api.onchange('bom_id')
    # def _onchange_bom_id(self):
    #     if self.bom_id:
    #         self.load_material_lines()
    #
    #
    # @api.onchange('quantity')
    # def _onchange_quantity(self):
    #     self.load_material_lines()
    #
    # @api.onchange('product_id')
    # def _onchange_product_id(self):
    #     if self.product_id:
    #         bom=self.env['mrp.bom'].search([('product_tmpl_id','=',self.product_id.product_tmpl_id.id)],limit=1)
    #     self.bom_id=bom
    #
    #
    # def load_material_lines(self):
    #     commands=[fields.command.clear()]
    #     if not self.bom_id:
    #         return {
    #             "warning":{'title':'warning','message':'Please select a bom'},
    #         }
    #     for line in self.bom_id.bom_line_ids:
    #         commands.append(fields.command.create(
    #             {
    #                 "product_id":line.product_id.id,
    #                 'required_qty':line.product_qty*self.quantity,
    #             }
    #         ))
    #     self.material_line_ids = commands
    #
    #
    # def action_confirm(self):
    #     for rec in self:
    #         if not rec.bom_id:
    #             raise ValidationError("Please select a bom")
    #         if rec.qantity<=0:
    #             raise ValidationError("Please select a bom")
    #         rec.state='confirmed'
    #
    # def action_start(self):
    #     for rec in self:
    #         if not rec.is_material_availablle:
    #             raise ValidationError("Please select material")
    #         rec.state='progress'

