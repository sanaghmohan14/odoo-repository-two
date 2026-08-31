from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    amount_limit=fields.Float(string="Amount Limit")


    @api.model
    def _load_pos_data_fields(self,config):
        print("self",self)
        print("config",config)

        data=super()._load_pos_data_fields(config)
        data.append('amount_limit')
        print("data123",data)

        return data