
from odoo import models,fields,api

from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    _description = "Sale Order"


    revision_id = fields.One2many('revision.tracking','sale_order_id',string="Revision History")

    def write(self, vals):

        for rec in self:
            # if rec.state == 'sent':
            # print(vals, "123vals")
            # print("testts")
            # if rec.order_id.state!='sent':
            #     continue
            # changes=[]
            #         changed_names1={
            #         'product_uom_qty':'quantity changed',
            #         'price_unit':'price changed'
            #         }
            old_product = rec.product_template_id.name
            print(old_product)
            old_quantity = rec.product_uom_qty
            old_price = rec.price_unit
            print(old_price)
            result = super(SaleOrderLine, rec).write(vals)

            changes = []

            new_product = rec.product_template_id.name
            new_quantity = rec.product_uom_qty
            new_price = rec.price_unit
            print(new_price)

            print('*' * 100, vals)

            if 'product_template_id' in vals and old_product != new_product:
                changes.append((f"product:{old_product} to {new_product}"))
            if 'product_uom_qty' in vals and old_quantity != new_quantity:
                changes.append((f"quantity:{new_product} {old_quantity} to {new_quantity}"))
            if 'price_unit' in vals and old_price != new_price:
                changes.append((f"price:{new_product} {old_price} to {new_price}"))

            print("Changes:", changes)

            if changes:
                # reason=rec.order_id.revision_notes
                # print('reason :',reason)
                # if  not reason:
                # raise ValidationError("no changes")
                notes = "\n".join(changes)
                print('notes :', notes)
                self.env['revision.tracking'].create({
                    'sale_id': rec.order_id.id,
                    'sale_order_id': rec.id,
                    'modified_on': fields.Datetime.now(),
                    'modified_by': self.env.user.id,
                    'revision_notes': notes,
                })
            return result





    # def action_product_history(self):
    #     print("hi 02938764")
    #     return{
    #         "type": "ir.actions.act_window",
    #         "name": "sale change",
    #         "res_model": "revision.tracking",
    #         "view_mode": "list,form",
    #         "domain":[('sale_order_id','=',self.id)]
    #
    #     }





    @api.model_create_multi
    def create(self, vals_list):

        lines=super().create(vals_list)
        for line in lines:
            if line.order_id.state=='sent':
                product_name=line.product_template_id.name
                print(product_name)

                note=f"Product added {product_name}"

                self.env['revision.tracking'].create({
                    'sale_id': line.order_id.id,
                    'sale_order_id': line.id,
                    'modified_on': fields.Datetime.now(),
                    'modified_by': self.env.user.id,
                    'revision_notes': note,
                })
        return  lines



    def unlink(self):
        for line in self:
            print("line present")
            if line.order_id.state == 'sent':
                print("1234567")
                product_name = line.product_template_id.name
                print(product_name)

                note=f"Product removed {product_name}"

                self.env['revision.tracking'].create({
                    'sale_id': line.order_id.id,
                    'sale_order_id': line.id,
                    'modified_on': fields.Datetime.now(),
                    'modified_by': self.env.user.id,
                    'revision_notes': note,
                })
        return super().unlink()






























