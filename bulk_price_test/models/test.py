# from odoo import models, fields
#
#
# class ProductProduct(models.Model):
#     _inherit = "product.product"
#
#     alternate_component_ids = fields.Many2many(
#         "product.product",
#         "product_component_alternate_rel",
#         "component_id",
#         "alternate_component_id",
#         string="Alternate Components",
#     )
#
#
#
#
#
#
#
#
#
# from odoo import models, fields
#
#
# class StockMove(models.Model):
#     _inherit = "stock.move"
#
#     suggested_alternate_id = fields.Many2one(
#         "product.product",
#         string="Choose Alternate",
#     )
#
#
#
#
#
#
#
# from odoo import models, fields
# from odoo.exceptions import UserError
#
#
# class MrpProduction(models.Model):
#     _inherit = "mrp.production"
#
#     def action_suggest_alternate(self):
#         self.ensure_one()
#
#         # Only consider active raw material moves (skip done/cancelled)
#         candidate_moves = self.move_raw_ids.filtered(
#             lambda move: move.state not in ("done", "cancel")
#         )
#
#         unavailable_moves = candidate_moves.filtered(
#             lambda move: move.product_id.qty_available < move.product_uom_qty
#         )
#
#         if not unavailable_moves:
#             raise UserError("All components have sufficient stock available.")
#
#         return {
#             "type": "ir.actions.act_window",
#             "name": "Suggest Alternate Components",
#             "res_model": "mrp.suggest.alternative.component",
#             "view_mode": "form",
#             "target": "new",
#             "context": {
#                 "default_order_id": self.id,
#                 "default_unavailable_component_ids": unavailable_moves.ids,
#             },
#         }








from odoo import models, fields
from odoo.exceptions import UserError




#
# class MrpSuggestAlternativeComponent(models.TransientModel):
#     _name = "mrp.suggest.alternative.component"
#     _description = "Suggest Alternate Component"
#
#     order_id = fields.Many2one(
#         "mrp.production",
#         string="Manufacturing Order",
#         required=True,
#     )
#
#     unavailable_component_ids = fields.Many2many(
#         "stock.move",
#         string="Unavailable Components",
#     )
#
#     def add_component(self):
#         self.ensure_one()
#
#         lines_to_process = self.unavailable_component_ids.filtered(
#             "suggested_alternate_id"
#         )
#
#         if not lines_to_process:
#             raise UserError(
#                 "Please select at least one alternate component before proceeding."
#             )
#
#         unlink_commands = []
#         create_commands = []
#
#         for move in lines_to_process:
#             unlink_commands.append(fields.Command.unlink(move.id))
#             create_commands.append(
#                 fields.Command.create({
#                     "product_id": move.suggested_alternate_id.id,
#                     "product_uom_qty": move.product_uom_qty,
#                     "product_uom": move.product_uom.id,
#                     "name": move.suggested_alternate_id.display_name,
#                 })
#             )
#
#         self.order_id.write({
#             "move_raw_ids": unlink_commands + create_commands
#         })
#
#         return {
#             "type": "ir.actions.client",
#             "tag": "reload",
#         }





