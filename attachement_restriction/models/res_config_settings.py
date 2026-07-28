from odoo import api, fields, models
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    require_attachment = fields.Boolean(string="Require Attachment")




    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('attachement_restriction.require_attachment', self.require_attachment)
        return res


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        with_user = self.env['ir.config_parameter'].sudo()

        com_contacts = with_user.get_param('attachement_restriction.require_attachment')

        res.update(require_attachment=[(6, 0, literal_eval(com_contacts))] if com_contacts else False, )
        return res