
from odoo import models,fields

from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    _description = "Sale Order"


    revision_id = fields.One2many('revision.tracking','sale_order_id',string="Revision History")




    # def write(self, vals):
    #     """used to change the price of product template"""
    #     # if self.state =='sent':
    #
    #     print('testttttt',vals)
    #     for rec in self:
    #         old_price=rec.price_unit
    #         old_quantity=rec.product_uom_qty
    #         print(old_price,'oldprice')
    #         print(old_quantity,'oldquantity')
    #         changes1=[]
    #
    #         changed_names1={
    #         'product_uom_qty':'quantity changed',
    #         'price_unit':'price changed'
    #         }
    #
    #         result = super(SaleOrderLine, rec).write(vals)
    #         if 'order_line.product_uom_qty' in vals:
    #             changes1.append(changed_names1['product_uom_qty'])
    #         if 'order_line.price_unit' in vals:
    #             changes1.append(changed_names1['price_unit'])
    #         print(changes1)
    #         string=",".join(changes1)
    #         print(string)
    #         if 'order_line.product_uom_qty' in vals or 'order_line.price_unit' in vals:
    #             # string = ",".join(old_quantity, "to",vals.product_uom_qty,old_price,"to",vals.price_unit)
    #
    #
    #             self.env['revision.tracking'].create({
    #                 'sale_order_id': self.id,
    #                 'modified_on': fields.Date.today(),
    #                 'modified_by': self.env.user.id,
    #                 'revision_notes': string,
    #
    #             })
    #
    #
    #     return result

    def write(self,vals):
        for rec in self:
            if rec.order_id.state!='sent':
                continue
            changes=[]
            #         changed_names1={
            #         'product_uom_qty':'quantity changed',
            #         'price_unit':'price changed'
            #         }
            old_product=rec.product_template_id.name
            print(old_product)
            old_quantity=rec.product_uom_qty
            old_price=rec.price_unit
            print(old_price)
            result=super(SaleOrderLine, rec).write(vals)
            new_product=rec.product_template_id.display_name
            new_quantity=rec.product_uom_qty
            new_price=rec.price_unit
            print(new_price)

            if 'product_template_id' in vals and old_product!=new_product:
                changes.append((f"product:{old_product} to {new_product}"))
            if 'product_uom_qty' in vals and old_quantity!=new_quantity:
                changes.append((f"quantity:{old_quantity} to {new_quantity}"))
            if 'price_unit' in vals and old_price!=new_price:
                changes.append((f"price:{old_price} to {new_price}"))

            print("Changes:",changes)

            if changes:
                if not  rec.order_id.revision_notes:
                    raise ValidationError("no changes")
                revision_notes = "\n".join(changes)
                self.env['revision.tracking'].create({
                    'sale_id':rec.order_id.id,
                    'sale_order_id':rec.id,
                    'modified_on':fields.Datetime.now(),
                    'revision_notes':revision_notes,
                })
            return result





    def action_product_history(self):
        print("hi 02938764")
        return{
            "type": "ir.actions.act_window",
            "name": "sale change",
            "res_model": "revision.tracking",
            "view_mode": "list,form",
            "domain":[('sale_order_id','=',self.id)]

        }