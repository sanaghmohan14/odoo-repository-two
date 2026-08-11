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





    #
    def write(self, vals):
        """used to change the price of product template"""
        # if self.state =='sent':
        for rec in self:
            changes = []
            changed_names = {
                'validity_date': 'changed expiry date',
                'date_order': 'changed date order',
                'payment_term_id': 'changed payment term',
                'partner_id': 'changed partner',
            }

            old_values = {}
            for field_name in changed_names:

                if field_name in vals:
                    old_value = rec[field_name]
                    if rec._fields[field_name].type == 'many2one':
                        if old_value:

                            old_values[field_name]=old_value.name
                        else:
                            old_values[field_name] = " "
                    else:
                        if old_values:

                            old_values[field_name] = str(old_value)
                        else:
                            old_values[field_name] = ""

            result = super(SaleOrder, rec).write(vals)

            print("items",changed_names.items())

            for field_name, field_label in changed_names.items():
                if field_name in vals:
                    new_value = rec[field_name]
                    if rec._fields[field_name].type == 'many2one':
                        if new_value:
                            new_value = new_value.name
                        else:
                            new_value = ""
                    else:
                        if new_value:
                            new_value = str(new_value)
                        else:
                            new_value = ""



                    old_value = old_values.get(field_name, '')

                    if old_value != new_value:
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




    def action_confirm(self):
        for rec in self:
            if 'validity_date' in rec:
                self.env['revision.tracking'].create({
                    'sale_id': self.id,
                    'modified_on': fields.Date.today(),
                    'modified_by': self.env.user.id,
                    'revision_notes': rec.revision_notes,
                })




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

