from odoo import api, fields, models,_

from odoo.exceptions import ValidationError


class MergeWizard(models.TransientModel):
    _name = 'merge.wizard'




    target_order_id = fields.Many2one('sale.order', string="Target Order")

    partner_id = fields.Many2one('res.partner', string="Customer")

    order_ids=fields.Many2many('sale.order')






    def wizard_merge(self):
        self.ensure_one()

        if not self.order_ids:
            raise ValidationError("Please select at least one order")


        different_partner=self.order_ids.filtered(lambda r: r.partner_id != self.partner_id)
        print("not equal partner",different_partner)



        if different_partner:
            raise ValidationError("not same partner")
        target=self.target_order_id

        first_order=self.order_ids[0]

        print("first order",first_order)
        # print(first_order.date_order)

        target.write(
            {
                'date_order':first_order.date_order,
                'validity_date':first_order.validity_date,
                'payment_term_id':first_order.payment_term_id.id,
            }
        )

        product_lines={
            line.product_id.id : line for line in target.order_line if line.product_id
        }



        for order in self.order_ids:

            for line in order.order_line:

                # if [line.product_id,line.product_id.id] in product_lines:

                if line.product_id and line.product_id.id in product_lines:

                    product_lines[line.product_id.id].product_uom_qty += line.product_uom_qty
                else:
                    new_line=line.copy({
                        'order_id': target.id
                    })

                    print("new line88888888888888888888888888888888888",new_line)

                    if new_line.product_id:
                        product_lines[new_line.product_id.id]=new_line

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': target.id,
            'target': 'current',
        }






