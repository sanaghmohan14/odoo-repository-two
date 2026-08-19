from odoo import models,fields,api
from odoo.exceptions import ValidationError



class ResPartner(models.Model):
    _inherit = "res.partner"


    # multiple_sale_order_ids = fields.Many2many('sale.order', string="Multiple Sale Order",)





    sale_order_ids=fields.One2many('sale.order','partner_id',string="Sale Orders")

    sale_product_count = fields.Integer(compute="_compute_sale_product_count",store=True)

    product_history = fields.Char()

    sale_history = fields.Char(string="Sale History")

    target_order_id = fields.Many2one('sale.order', string="Target Order")


    # def compute_partner(self):
    #     for rec in self:
    #         rec.partner_id = self.id




    def _compute_sale_product_count(self):
        for partner in self:
            lines=self.env['sale.order.line'].search([
                ('order_id.partner_id','=',partner.id)])

            partner.sale_product_count = len(lines.product_id)



    def action_view_sold_product(self):
        self.ensure_one()
        lines = self.env['sale.order.line'].search([
            ('order_id.partner_id', '=', self.id), ])
        print(len(lines))

        products=lines.product_id

        return{
            # 'name':'product sold to %s' %(self.name or ''),
            'name':' products.name',
            'type': 'ir.actions.act_window',
            'res_model':'product.product',
            'view_mode':'list,form',
            'target': 'current',
            'domain': [('id','in',products.ids)],
        }


    # def action_product_history(self):
    #     for rec in self:
    #         for i in self.multiple_sale_order_ids:
    #             print(i)
    #             print(len(self.multiple_sale_order_ids))
    #
    #             target=self.multiple_sale_order_ids
    #             #
    #             # product_lines = {
    #             #     line.product_id.id: line for line in target.order_line if line.product_id
    #             # }
    #
    #             # print(product_lines,"my products")
    #
    #             count=0
    #             for order in self.multiple_sale_order_ids:
    #                 for line in order.order_line:
    #                     if line.product_id:
    #                         print(line.product_id.name)
    #                         count+=1
    #             print(count, "count")
    #             rec.product_count = count
    #
    #
    #             return{
    #                 'type':'ir.actions.act_window',
    #                 'res_model':'product.template',
    #                 'view_mode':'list,form',
    #                 'target': 'current'
    #             }





    #
    #
    # def action_sale_history_one(self):
    #     """this function is used to show the list form of service history for a customer in customer form"""
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'sale_history',
    #         'res_model': 'sale.order',
    #         'domain': [('partner_id', '=',self.id)],
    #         'view_mode': 'list,form',
    #         'view_type': 'form',
    #         # 'context':{'search_default_order':'end_date asc'}
    #
    #     }









