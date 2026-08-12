from os import WCONTINUED

from odoo import models,fields

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    _description = "Sale Order Multiple Invoices"


    revision_id = fields.One2many('revision.tracking','sale_id',string="Revision History")


    revision_notes = fields.Char(string="Reason For Change")
    # rev_count = fields.Integer(string="Revision Count", compute='_compute_revision_count', store=True)
    revision_history = fields.Char(string="Revision History")

    revision_count = fields.Integer(string="Revision Count",compute='compute_revision_count_one')


    # def action_product_history(self):
    #     print("hi")






    # def write(self, vals):
    #     """used to change the price of product template"""
    #     # if self.state =='sent':
    #     print(vals,"values of j")
    #     for rec in self:
    #         changes = []
    #         changed_names = {
    #             'validity_date': 'changed expiry date',
    #             'date_order': 'changed date order',
    #             'payment_term_id': 'changed payment term',
    #             'partner_id': 'changed partner',
    #         }
    #
    #
    #
    #         old_values = {}
    #         for field_name in changed_names:
    #
    #             if field_name in vals:
    #                 old_value = rec[field_name]
    #                 print('test :',rec._fields[field_name].type)
    #                 if rec._fields[field_name].type == 'many2one':
    #                     if old_value:
    #
    #                         old_values[field_name]=old_value.name
    #                     else:
    #                         old_values[field_name] = " "
    #                 else:
    #                     if old_values:
    #
    #                         old_values[field_name] = str(old_value)
    #                     else:
    #                         old_values[field_name] = ""
    #
    #         result = super(SaleOrder, rec).write(vals)
    #
    #         print("items",changed_names.items())
    #
    #         for field_name, field_label in changed_names.items():
    #             if field_name in vals:
    #                 new_value = rec[field_name]
    #                 if rec._fields[field_name].type == 'many2one':
    #                     if new_value:
    #                         new_value = new_value.name
    #                     else:
    #                         new_value = ""
    #                 else:
    #                     if new_value:
    #                         new_value = str(new_value)
    #                     else:
    #                         new_value = ""
    #
    #
    #
    #                 old_value = old_values.get(field_name, '')
    #
    #                 if old_value != new_value:
    #                     changes.append(f"{field_label}:"f"{old_value} to {new_value}")
    #
    #         print(changes)
    #
    #         # if changes and not rec.revision_notes:
    #         #     raise ValidationError("no")
    #
    #         if changes:
    #             revision_notes = "\n".join(changes)
    #             self.env['revision.tracking'].create({
    #                 'sale_id': rec.id,
    #                 'modified_on': fields.Date.today(),
    #                 'modified_by': self.env.user.id,
    #                 'revision_notes': revision_notes,
    #
    #             })
    #     return result



    def write(self, vals):
        """used to change the price of product template"""
        # if self.state =='sent':

        # if self.state != 'draftt':
        for rec in self:


            # if rec.state == 'sent':
            #     continue

            changes = []
            old_values = {}

            new_vals = vals.copy()
            print(new_vals, "4444444444444444")

            new_vals.pop('order_line', 'None')

            for field_name in new_vals:

                # if field_name in vals:
                if field_name not in rec._fields:
                    continue
                old_value = rec[field_name]
                field_type = rec._fields[field_name].type

                if field_type == 'many2one':
                    if old_value:
                        old_values[field_name] = old_value.name
                    else:
                        old_values[field_name] = " "

                elif field_type in ['one2many', 'many2one']:
                    old_values[field_name] = str(old_value.ids)

                else:
                    if old_value:
                        old_values[field_name] = str(old_value)
                    else:
                        old_values[field_name] = " "

            result = super(SaleOrder, rec).write(vals)

            for field_name in new_vals:
                if field_name not in rec._fields:
                    continue

                new_value = rec[field_name]

                field_type = rec._fields[field_name].type

                if field_type == 'many2one':
                    if new_value:
                        new_value = new_value.name
                    else:
                        new_value = ""
                elif field_type in ['one2many', 'many2one']:
                    new_value = str(new_value.ids)
                else:
                    if new_value:
                        new_value = str(new_value)
                    else:
                        new_value = ""
                old_value = old_values.get(field_name, '')

                if old_value != new_value:
                    field_label = rec._fields[field_name].string

                    changes.append(f"{field_label}:"f"{old_value} to {new_value}")
                print(changes)


            # if changes and not rec.revision_notes:
            #     raise ValidationError("no")

            if changes:
                revision_notes = "\n".join(changes)
                self.env['revision.tracking'].create({
                    'sale_id': rec.id,
                    'modified_on': fields.Date.today(),
                    'modified_by': self.env.user.id,
                    'revision_notes': revision_notes,

                })
            return result











    # def action_confirm(self):
    #     for rec in self:
    #         if 'validity_date' in rec:
    #             self.env['revision.tracking'].create({
    #                 'sale_id': self.id,
    #                 'modified_on': fields.Date.today(),
    #                 'modified_by': self.env.user.id,
    #                 'revision_notes': rec.revision_notes,
    #             })




    def action_product_history(self):
        print("hi 02938764")
        return{
            "type": "ir.actions.act_window",
            "name": "sale change",
            "res_model": "revision.tracking",
            "view_mode": "list,form",
            "domain":[('sale_id','=',self.id)]

        }



    # def _compute_revision_count(self):
    #     for rec in self:
    #         rec.revision_count = len(rec.revision_id)
    #         print(rec.rev_count)

    def compute_revision_count_one(self):
        for rec in self:
            rec.revision_count = len(rec.revision_id)

