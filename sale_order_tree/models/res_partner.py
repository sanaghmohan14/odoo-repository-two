from odoo import models,fields,api
from odoo.exceptions import ValidationError



class ResPartner(models.Model):
    _inherit = "res.partner"


    multiple_sale_order_ids = fields.Many2many('sale.order', string="Multiple Sale Order",)

    # allowed_alternate_id = fields.Many2many('sale.order',
    #                                         related='  multiple_sale_order_ids.product_id',
    #                                         string="Alternate ")

                                               # domain=[('partner_id', '==','id')])

    #
    # target_order_id = fields.Many2one('sale.order', string="Target Order")

    partner_id = fields.Many2one('res.partner',
                                 relation="partner_one",
                                 column1="part_id",
                                 column2="part_two_id",
                                 string="Customer")
    product_count = fields.Integer(stirng="Product Count")

    sale_count = fields.Integer(compute="compute_sale_count",store=True)

    product_history = fields.Char()

    sale_history = fields.Char(string="Sale History")

    target_order_id = fields.Many2one('sale.order', string="Target Order")


    # def compute_partner(self):
    #     for rec in self:
    #         rec.partner_id = self.id






    def action_product_history(self):
        for rec in self:
            for i in self.multiple_sale_order_ids:
                print(i)
                print(len(self.multiple_sale_order_ids))

                target=self.multiple_sale_order_ids
                #
                # product_lines = {
                #     line.product_id.id: line for line in target.order_line if line.product_id
                # }

                # print(product_lines,"my products")

                count=0
                for order in self.multiple_sale_order_ids:
                    for line in order.order_line:
                        if line.product_id:
                            print(line.product_id.name)
                            count+=1
                print(count, "count")
                rec.product_count = count







                return{
                    'type':'ir.actions.act_window',
                    'res_model':'product.template',
                    'view_mode':'form',
                    'target': 'current'
                }




















    def _compute_count(self):
        print("one")


    def action_sale_history_one(self):
        """this function is used to show the list form of service history for a customer in customer form"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'sale_history',
            'res_model': 'sale.order',
            'domain': [('partner_id', '=',self.id)],
            'view_mode': 'list,form',
            'view_type': 'form',
            # 'context':{'search_default_order':'end_date asc'}

        }

    def compute_sale_count(self):
        for rec in self:
            rec.sale_count = len(rec.multiple_sale_order_ids)


    # def compute_product_count(self):
    #     for rec in self:
    #         rec.product_count=








