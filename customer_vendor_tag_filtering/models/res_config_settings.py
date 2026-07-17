from odoo import api, fields, models
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customer_tag_ids = fields.Many2many(related="company_id.customer_tag_ids",readonly=False,string="Customer Tags")
    vendor_tag_ids = fields.Many2many(related="company_id.vendor_tag_ids",readonly=False,string="Vendor Tags")










    # def set_values(self):
    #     res = super(ResConfigSettings, self).set_values()
    #     self.env['ir.config_parameter'].sudo().set_param('customer_vendor_tag_filtering.customer_tag_ids', self.customer_tag_ids.ids)
    #     self.env['ir.config_parameter'].sudo().set_param('customer_vendor_tag_filtering.vendor_tag_ids', self.vendor_tag_ids.ids)
    #     return res
    #
    #
    #
    #
    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     with_user = self.env['ir.config_parameter'].sudo()
    #     com_contacts = with_user.get_param('customer_vendor_tag_filtering.customer_tag_ids')
    #     vendor_contacts = with_user.get_param('customer_vendor_tag_filtering.vendor_tag_ids')
    #     res.update(customer_tag_ids=[(6, 0, literal_eval(com_contacts))
    #                                ] if com_contacts else False, )
    #     res.update(vendor_tag_ids=[(6, 0, literal_eval(vendor_contacts))
    #                              ] if vendor_contacts else False, )
    #     return res