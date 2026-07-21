from odoo import api, fields, models


class BulkPrice(models.Model):
    _name = 'bulk.price'


    product_ids = fields.Many2many('product.product',string="Product")

    price_update_type = fields.Selection([('percentage','percentage'),('fixedprice','fixedprice')],string="Update Price",default='fixedprice')

    product_price = fields.Float(string="Price")
