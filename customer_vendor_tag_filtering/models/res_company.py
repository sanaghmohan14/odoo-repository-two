from odoo import api, fields, models
from odoo.orm.decorators import readonly


class ResCompany(models.Model):
    _inherit = 'res.company'


    customer_tag_ids = fields.Many2many("res.partner.category",string="Customer Tags",relation="my_model_res_company_rel_1")

    vendor_tag_ids  = fields.Many2many("res.partner.category",string="Vendor Tags",relation="my_model_res_company_rel_2")