# from odoo import models, fields
#
#
# class ProductTemplate(models.Model):
#     _inherit = "product.template"
#
#     alternate_product_ids = fields.Many2many(
#         "product.product",
#         string="Approved Alternate Products"
#     )
#
#
# from odoo import models, fields
#
#
# class AlternateProductWizard(models.TransientModel):
#     _name = "alternate.product.wizard"
#     _description = "Alternate Product Wizard"
#
#     move_id = fields.Many2one(
#         "stock.move",
#         string="Component",
#         required=True
#     )
#
#     product_id = fields.Many2one(
#         "product.product",
#         string="Current Product",
#         readonly=True
#     )
#
#     required_qty = fields.Float(
#         string="Required Quantity",
#         readonly=True
#     )
#
#     alternate_product_id = fields.Many2one(
#         "product.product",
#         string="Alternate Product",
#         required=True,
#         domain="[('id', 'in', product_id.product_tmpl_id.alternate_product_ids)]"
#     )
#
#     def action_replace(self):
#         self.ensure_one()
#
#         self.move_id.write({
#             "product_id": self.alternate_product_id.id
#         })
#
#         return {
#             "type": "ir.actions.act_window_close"
#         }
#
#
# from odoo import models
# from odoo.exceptions import UserError
#
#
# class StockMove(models.Model):
#     _inherit = "stock.move"
#
#     def action_suggest_alternate(self):
#         self.ensure_one()
#
#         if self.product_id.qty_available >= self.product_uom_qty:
#             raise UserError(
#                 "This component has enough stock. "
#                 "Alternate is not required."
#             )
#
#         return {
#             "type": "ir.actions.act_window",
#             "name": "Suggest Alternate",
#             "res_model": "alternate.product.wizard",
#             "view_mode": "form",
#             "target": "new",
#             "context": {
#                 "default_move_id": self.id,
#                 "default_product_id": self.product_id.id,
#                 "default_required_qty": self.product_uom_qty,
#             },
#         }
#
#
#
