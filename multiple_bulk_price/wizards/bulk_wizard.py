from odoo import api, fields, models,_

from odoo.exceptions import ValidationError


class BulkWizard(models.TransientModel):
    _name = 'bulk.wizard'


    product_ids = fields.Many2many('product.product',string="Product")

    price_update_type = fields.Selection([('percentage','percentage'),('fixedprice','fixedprice')],string="Update Price",default='fixedprice')

    product_price = fields.Float(string="Price")




    def action_apply(self):
        print("hi")

        summary=""
        for product in self.product_ids:
            print("hi")
            if self.price_update_type=="percentage":
                print("working")
                new_price=product.list_price+(product.list_price*self.product_price/100)
                print("new_price",new_price)
            else:
                new_price=self.product_price
                print("new_price",new_price)
            product.list_price=new_price

            # summary = summary+(product.name,new_price)
        summary="product price updated"


        return {'type': 'ir.actions.client',
                    'tag':'display_notification',
                    'params':{
                        'message': _("product price updated"),
                    }
                }