from odoo import models,fields

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    _description = "Sale Order Multiple Invoices"


    revision_id = fields.One2many('revision.tracking','sale_id',string="Revision History")


    revision_notes = fields.Char(string="Reason For Change")


    # def action_product_history(self):
    #     print("hi")

    def write(self, vals):
        """used to change the price of product template"""
        # if self.state =='sent':
        for rec in self:

            old_date = rec.validity_date

            print(old_date, "old")

            changes=[]
            changed_names={
                'expiration_date':'changed expiry date',
                'date_order':'changed date order',
                'payment_term_id':'changed payment term',
                'partner_id':'changed partner',
            }
            s=",".join(changes)
            print(s)


            # for names in changed_names.items():
            #     print(names)
            #     changes.append(names)
            # print(changes)

            result = super(SaleOrder, rec).write(vals)


            if 'validity_date' in vals:
                changes.append(str(changed_names['expiration_date']))
                # changes.append("payment_term_id")
            if 'payment_term_id' in vals:
                changes.append(changed_names['payment_term_id'])
            if 'partner_id' in vals:
                changes.append(changed_names['partner_id'])
            if 'date_order' in vals:
                changes.append(changed_names['date_order'])



            s = ",".join(changes)
            print(s)

            print(str(changes))


            if not self.revision_notes:
                raise ValidationError("please set reason")

            if 'validity_date' in vals or 'date_order' in vals or 'payment_term_id' in vals or 'partner_id' in vals:

                self.env['revision.tracking'].create({
                    'sale_id': self.id,
                    'modified_on': fields.Date.today(),
                    'modified_by': self.env.user.id,
                    'revision_notes': s,

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