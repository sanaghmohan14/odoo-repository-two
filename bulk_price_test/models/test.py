# # @api.onchange('bom_id')
# def _onchange_bom_id(self):
#     if self.bom_id:
#         self.load_material_lines()
#
# @api.onchange('quantity')
# def _onchange_quantity(self):
#     self.load_material_lines()
#
# @api.onchange('product_id')
# def _onchange_product_id(self):
#     if self.product_id:
#         bom = self.env['mrp.bom'].search([('product_tmpl_id','=',self.product_id.product_tmpl_id.id)],limit=1)
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







# @api.depends('material_line_ids.consumed_qty', 'material_line_ids.required_qty')
# def _compute_material_total(self):
#     for rec in self:
#         rec.total_consumed = sum(rec.material_line_ids.mapped('consumed_qty'))
#         rec.remaing_material = sum(line.required_qty - line.consumed_qty for line in rec.material_line_ids)