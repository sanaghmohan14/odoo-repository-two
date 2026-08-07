from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
from odoo.exceptions import RedirectWarning


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
            if not self.reason_to_change:
                raise ValidationError("please set reason")

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



    # def write(self, vals):
    #     """used to change the price of product template"""
    #     for rec in self:
    #         old_price=rec.list_price
    #         print(old_price,"old")
    #
    #         result = super(ProductTemplate,rec).write(vals)
    #         # if not self.reason_to_change:
    #         #     raise ValidationError("please set reason")
    #
    #         if 'list_price' in vals:
    #
    #             self.env['product.service.history'].create({
    #                 'product_id': self.id,
    #                 'previous_price': old_price,
    #                 'new_price': rec.list_price,
    #                 'changed_by': self.env.user.id,
    #                 'changed_date': fields.Date.today(),
    #                 # 'reason_to_change':rec.reason_to_change,
    #             })
    #
    #             # view_item = [(self.env.ref('product_price_change.price_change_wizard').id, 'form')]
    #             # view = self.env.ref('product_price_change.price_change_wizard')
    #             print('asfdasdfasdf')
    #             return {
    #                 'type': 'ir.actions.act_window',
    #                 'res_model': 'price.change.wizard',
    #                 'view_mode': 'form',
    #                 'name': _("TEST"),
    #                 'target': 'current',
    #                 'views': [(False, 'form')],
    #             }



    def action_product_history(self):
        print("hi 02938764")
        return{
            "type": "ir.actions.act_window",
            "name": "Product History",
            "res_model": "product.service.history",
            "view_mode": "list,form",
            "domain":[('product_id','=',self.id)]

        }



    def action_change_price(self):
        print("ji")
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'price.change.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context':{
                "default_product_id": self.id,
                "default_new_price": self.list_price,
            }
        }




    #
    # @api.model
    # def create(self, vals):
    #     res=super().create(vals)
    #     view_item = self.env.ref('product_price_change.price_change_wizard')
    #     msg='wizard'
    #     if vals:
    #
    #         raise RedirectWarning(msg, view_item.id, _('Go to the wizard'),
    #                           {'active_id': self._origin.id, })




















