from odoo import models,fields,api
from odoo.release import description
import logging



class CrmLead(models.Model):
    _inherit = "crm.lead"

    _logger = logging.getLogger(__name__)


    xxx=fields.Char(string="nanmmemmemem")



    @api.onchange('user_id')
    def _onchange_user_id(self):
        if not self.tag_ids:
            return

        users = self.env['res.users'].search([('tag_ids', 'in', self.tag_ids)])

        for user in users:
            generated_leads = self.search_count([
                ('user_id', '=', user.id),
                ('type', '=', 'lead'),
                ('active', '=', True),
            ])

            if generated_leads <= 3:
                self.user_id = user.id
                break
