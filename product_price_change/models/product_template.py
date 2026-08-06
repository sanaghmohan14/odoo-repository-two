from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class ProductTemplate(models.Model):
    _inherit = "product.template"


    service_id = fields.One2many('product.service.history','product_id',string="Service History")


    reason_to_change = fields.Char(string="Reason For Change")


    def write(self, vals):
        """used to change the price of product template"""
        for rec in self:
            old_price=rec.list_price
            print(old_price,"old")
            result = super(ProductTemplate,rec).write(vals)
            if 'list_price' in vals:
                self.env['product.service.history'].create({
                    'product_id':self.id,
                    'previous_price':old_price,
                    'new_price':rec.list_price,
                    'changed_by':self.env.user.id,
                    'changed_date':fields.Date.today(),
                    'reason_to_change':rec.reason_to_change,
                })

        return result





    def action_product_history(self):
        print("hi 02938764")
        return{
            "type": "ir.actions.act_window",
            "name": "Product History",
            "res_model": "product.service.history",
            "view_mode": "list,form",
            "domain":[('product_id','=',self.id)]

        }




















