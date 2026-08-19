from odoo import models,fields,api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = "sale.order"


    multiple_sale_order_ids = fields.Many2many('sale.order', string="Multiple Sale Order",


                                            domain=[('state', '==', 'draft')])

    # ('order_id.state', '!=', 'cancel')