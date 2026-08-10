from odoo import models,fields

from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    _description = "Sale Order"


    revision_ids = fields.One2many('revision.tracking','sale_order_id',string="Revision History")





    def write(self, vals):
        """used to change the price of product template"""
        # if self.state =='sent':

        print('testttttt',vals)
        for rec in self:
            old_price=rec.price_unit
            old_quantity=rec.product_uom_qty
            print(old_price,'oldprice')
            print(old_quantity,'oldquantity')
            changes1=[]

            changed_names1={
            'product_uom_qty':'quantity changed',
            'price_unit':'price changed'
            }


            result = super(SaleOrderLine, rec).write(vals)

            if 'product_uom_qty' in vals:
                changes1.append(changed_names1['product_uom_qty'])
            if 'price_unit' in vals:
                changes1.append(changed_names1['price_unit'])
            print(changes1)

            string=",".join(changes1)
            print(string)


            if 'product_uom_qty' in vals or 'price_unit' in vals:
                # string = ",".join(old_quantity, "to",vals.product_uom_qty,old_price,"to",vals.price_unit)


                self.env['revision.tracking'].create({
                    'sale_order_id': self.id,
                    'modified_on': fields.Date.today(),
                    'modified_by': self.env.user.id,
                    'revision_notes': string,

                })


        return result