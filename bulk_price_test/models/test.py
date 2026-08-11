# def write(self, vals):
#
#     print(vals, "values of j")
#
#     for rec in self:
#
#         changes = []
#
#
#         old_values = {}
#
#         for field_name in vals:
#
#
#             if field_name not in rec._fields:
#                 continue
#
#             old_value = rec[field_name]
#
#             field_type = rec._fields[field_name].type
#
#             if field_type == 'many2one':
#
#                 if old_value:
#                     old_values[field_name] = old_value.display_name
#                 else:
#                     old_values[field_name] = ""
#
#             elif field_type in ['one2many', 'many2many']:
#
#                 old_values[field_name] = str(old_value.ids)
#
#             else:
#
#                 if old_value:
#                     old_values[field_name] = str(old_value)
#                 else:
#                     old_values[field_name] = ""
#
#         # Perform the actual write
#         result = super(SaleOrder, rec).write(vals)
#
#         # Get NEW values for every field in vals
#         for field_name in vals:
#
#             if field_name not in rec._fields:
#                 continue
#
#             new_value = rec[field_name]
#
#             field_type = rec._fields[field_name].type
#
#             if field_type == 'many2one':
#
#                 if new_value:
#                     new_value = new_value.display_name
#                 else:
#                     new_value = ""
#
#             elif field_type in ['one2many', 'many2many']:
#
#                 new_value = str(new_value.ids)
#
#             else:
#
#                 if new_value:
#                     new_value = str(new_value)
#                 else:
#                     new_value = ""
#
#             old_value = old_values.get(field_name, "")
#
#             # Only record if value actually changed
#             if old_value != new_value:
#
#                 field_label = rec._fields[field_name].string
#
#                 changes.append(
#                     f"{field_label}: {old_value} → {new_value}"
#                 )
#
#         print("CHANGES:", changes)
#
#         # Create revision history
#         if changes:
#
#             revision_notes = "\n".join(changes)
#
#             self.env['revision.tracking'].create({
#                 'sale_id': rec.id,
#                 'modified_on': fields.Datetime.now(),
#                 'modified_by': self.env.user.id,
#                 'revision_notes': revision_notes,
#             })
#
#     return result