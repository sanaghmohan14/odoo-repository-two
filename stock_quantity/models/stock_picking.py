from odoo import models,fields,api
from odoo.exceptions import ValidationError
from odoo.release import description



class SaleOrder(models.Model):
    _inherit = "stock.picking"


    total_quantity = fields.Float(string="Total Quantity",compute="_compute_total_quantity")

    #
    # multiple_stock_order_ids = fields.Many2many('stock.picking', string="Multiple stocks",
    #
    #                                           )

    multiple_stock_order_ids = fields.One2many('stock.picking', 'partner_id', string="Sale Orders",
                                               relation="stock_one_relation",
                                               column1="stock_one_id",
                                               column2="stock_three_id",
                                               )



    def _compute_total_quantity(self):
        for rec in self:
            if rec.move_line_ids:
                for i in rec.move_line_ids:
                    print("yes move lines")
                    count=sum(rec.move_line_ids.mapped('quantity'))
                    rec.total_quantity =count

            else:
                rec.total_quantity = 0




    def button_validate(self):
        print("theeern")
        for rec in self:
            print("rec")
            if rec.move_line_ids:
                print("i")
                length=len(rec.move_line_ids)

                for j in rec.move_line_ids:
                    quantity_one=sum(rec.move_line_ids.mapped('quantity'))
                    print("quantity",quantity_one)
                    if quantity_one>10:
                        raise ValidationError("quantity exceeded")
                print(length)
                if length>2:
                    raise ValidationError("More than two lines")

        return super().button_validate()





    def action_confirm(self):
        """this function is used to add multiple sale order lines in invoice"""
        #
        # self.invoice_line_ids = [(fields.Command.clear())]

        new = []
        for rec in self.multiple_stock_order_ids:

            new.append(fields.Command.create({
                    # 'name': rec.name,
                    'product_id': rec.product_id.id,
                    # 'quantity': rec.quantity,
                    # 'price_unit': rec.price_unit,
                }))

        self.move_line_ids = new
        return super().action_confirm()








