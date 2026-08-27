from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ProductProduct(models.Model):
    _inherit = "product.template"



    product_owner_id = fields.Many2one('res.partner',string="Product Owner")


    @api.model
    def _load_pos_data_fields(self,config):
        print("self",self)
        print("config",config)

        data=super()._load_pos_data_fields(config)
        data.append('product_owner_id')
        print("data",data)
        return data


