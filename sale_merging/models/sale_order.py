from odoo import models,fields,api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = "sale.order"

    multiple_sale_order_ids = fields.Many2many('sale.order', string="Multiple Sale Order",
                                               relation="sale_order_one",
                                               column1="sale_id",
                                               column2="sale_one_id",
                                               domain=[('state', '==', 'draft')])


    def action_merge(self):
        for rec in self:

            if rec.state == 'draft':
                print("state is in draft")
                # rec.order_line = [(fields.Command.clear())]

                new = []
                x=[]
                for j in self.multiple_sale_order_ids:
                    domination_date=j[0].date_order
                    exp_date=j[0].validity_date
                    payment_term=j[0].payment_term_id
                    print(payment_term)
                    print(domination_date,"domination Date")
                    print(exp_date,"exp Date")

                for  i in self:

                    self.write({
                        'date_order':domination_date,
                        'validity_date':exp_date,
                        'payment_term_id':payment_term,

                    })

                for i in self.multiple_sale_order_ids:
                    if i.partner_id == self.partner_id:

                        for rec in i.order_line:
                            new.append(fields.Command.create({
                            'name': rec.name,
                            'product_id': rec.product_id.id,
                            'product_uom_qty': rec.product_uom_qty,
                            'price_unit': rec.price_unit,

                        }))


                    else:
                        raise ValidationError("not same customer")
                self.order_line = new


    #



    # def action_merge(self):
    #     for rec in self:
    #
    #         if rec.state == 'draft':
    #             print("state is in draft")
    #             # rec.order_line = [(fields.Command.clear())]
    #
    #             new = []
    #             x = []
    #             for j in self.multiple_sale_order_ids:
    #                 domination_date = j[0].date_order
    #                 exp_date = j[0].validity_date
    #                 payment_term = j[0].payment_term_id
    #                 print(payment_term)
    #                 print(domination_date, "domination Date")
    #                 print(exp_date, "exp Date")
    #
    #
    #             # for k in self.multiple_sale_order_ids:
    #             #     print(k,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    #             #     products=self.env.ref('sale.sale_order_line').search([])
    #             #
    #             #     if k.product_template_id =
    #             #         print(k.product_id.product_uom_qty,"111111111111111111111111111111111111111111111")
    #             #         print(self.product_id.product_uom_qty,"22222222222222222222222222222222222222222222")
    #
    #
    #             for i in self:
    #                 self.write({
    #                     'date_order': domination_date,
    #                     'validity_date': exp_date,
    #                     'payment_term_id': payment_term,
    #
    #
    #                 })
    #
    #
    #             for i in self.multiple_sale_order_ids:
    #                 if i.partner_id == self.partner_id:
    #
    #
    #                     for rec in i.order_line:
    #                         new.append(fields.Command.create({
    #                             'name': rec.name,
    #                             'product_id': rec.product_id.id,
    #                             'product_uom_qty': rec.product_uom_qty,
    #                             'price_unit': rec.price_unit,
    #
    #                         }))
    #
    #
    #                 else:
    #                     raise ValidationError("not same customer")
    #             self.order_line = new


    def action_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "alternate",
            'res_model': 'merge.wizard',
            'view_mode': 'form',
            "target": "new",
            "context": {
                "default_order_id": self.id,


            }

        }













