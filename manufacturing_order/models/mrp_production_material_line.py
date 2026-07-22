from odoo import fields,models,api
from odoo.exceptions import ValidationError



class MrpProductionMaterial(models.Model):
    _name="mrp.production.material"
    _description = "production material"
    # _rec_name = "product_id"

    production_id = fields.Many2one('mrp.production.ext',string="Production Name")
    product_id = fields.Many2one('product.product',string="Materials Required")
    required_qty = fields.Float(string="Required Qty")
    available_qty = fields.Float(string="Available Qty")
    consumed_qty = fields.Float(string="Consumed Qty")
    is_material_available = fields.Boolean(string="Is Material Available")
    total_consumed = fields.Float(string="Total Consumed")
    remaing_material = fields.Float(string="Remaing Material")





    #
    # @api.depends('product_id')
    # def _compute_available_qty(self):
    #     for rec in self:
    #         rec.available_qty=rec.production_id.qty_available

