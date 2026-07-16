from odoo import models,fields,api

class CrmLead(models.Model):
    _inherit = "crm.lead"

    xxx=fields.Char(string="")





    # @api.onchange('tag_ids')
    # def _onchange_user_id(self):
    #
    #     if not self.tag_ids:
    #         return
    #
    #     users = self.env['res.users'].search([('skill_tag_ids', 'in', self.tag_ids.ids)],limit=1)
    #
    #     if users:
    #         self.user_id = users
    #
    #     print(users)




    @api.onchange('tag_ids')
    def _onchange_user_id(self):

        if not self.tag_ids:
            return

        users = self.env['res.users'].search([('skill_tag_ids', 'in', self.tag_ids.ids)], limit=1)


        for user in users:
            generated_leads = self.search_count([
                ('user_id', '=', user.id),('type', '=', 'lead'),
                ('stage_id.is_won','=',False),
            ])
            print(generated_leads)


            if generated_leads <= 3:
                self.user_id = user
                break
