from odoo import fields,models,api
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'



    def action_confirm(self):
        for rec in self:
            if rec.move_raw_ids:
                length=len(rec.move_raw_ids)
                print(length)
                if length>2:
                    raise ValidationError("More than one move in this production")
            else:
                return super().acttion



