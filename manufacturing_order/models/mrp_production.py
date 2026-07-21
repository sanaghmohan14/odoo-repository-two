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




    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('mrp.production.ext') or 'New'
            return super().create(vals_list)


    @api.onchange('bom_id')
    def _onchange_bom_id(self):
        if self.bom_id:

            self.unit_price = self.product_id.list_price
