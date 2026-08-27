# from odoo import api, fields, models
# from odoo.exceptions import ValidationError
#
#
# class BulkPrice(models.Model):
#     _name = 'bulk.price.update'
#
#
#     product_ids = fields.Many2many('product.product',string="Product")
#
#     price_update_type = fields.Selection([('percentage','percentage'),('fixedprice','fixedprice')],string="Update Price",default='fixedprice')
#
#     product_price = fields.Float(string="Price")
#
#     #
#     # def action_apply(self):
#     #     if not self.env.user.has_group('product.group_product_manager'):
#     #         raise ValidationError("")
#     #
#     #     summary=""
#     #     for product in self.product_ids:
#     #         if self.price_update_type=="percentage":
#     #             new_price=product.list_price+(product.list_price*self.value/100)
#     #         else:
#     #             new_price=self.value
#     #         product.list_price=new_price
#     #
#     #         summary += (product.name,new_price)
#     #
#     #       return {'type': 'ir.actions.client',
#     #                 'tag':'display_notification',
#     #                 'message': summary}



from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_owner_id = fields.Many2one("res.partner", string="Product Owner")

    @api.model
    def _load_pos_data_fields(self, config_id):
        data = super()._load_pos_data_fields(config_id)
        data.append("product_owner_id")
        return data