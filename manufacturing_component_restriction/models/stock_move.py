from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = "stock.move"



    suggested_alternate_id = fields.Many2one('product.product',string="Suggested Alternate Product")

    allowed_alternate_id = fields.Many2many('product.product',
                                           related='product_id.alternate_component_ids',
                                           string="Alternate Product")

    valid_alternate_ids = fields.Many2many('product.product',string="Valid Alterate Product",compute="_compute_valid_alterate_id")

    # allowed_product_id = fields.Float('product.product',related='product_id.qty_available',string="Alternate 1 Product")
    #
    # product_qty = fields.Float('stock.move',related='product_id.product_uom_qty',string="Quantity")

    @api.depends('product_id','product_uom_qty')
    def _compute_valid_alterate_id(self):
        for move in self:
            alternates = move.product_id.alternate_component_ids
            print("alternates",alternates)
            move.valid_alternate_ids =alternates.filtered(lambda a: a.qty_available >= move.product_uom_qty)
            print(move.valid_alternate_ids)


