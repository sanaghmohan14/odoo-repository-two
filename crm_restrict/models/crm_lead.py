from odoo import models,fields,api
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = "crm.lead"

    count = fields.Integer(string="Count",compute="_compute_count")



    def action_set_won_rainbowman(self):
        for rec in self:
            meeting_scheduled=self.env['calendar.event'].search_count([('opportunity_id','=',rec.id)])
            print(meeting_scheduled)
            if meeting_scheduled==0:
                if not self.env.user.has_group('sales_team.group_sale_manager'):
                    raise ValidationError("print no meeting")
        return super().action_set_won_rainbowman()



    def _compute_count(self):
        for rec in self:
            meeting_count=self.env['calendar.event'].search_count([('opportunity_id','=',rec.id)])
            rec.count=meeting_count












