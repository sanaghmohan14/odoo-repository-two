from odoo import api, fields, models
from odoo.exceptions import ValidationError
# from mimetypes import MimeType


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'




    def button_confirm(self):
        print("hi")

        mandatory = self.env['ir.config_parameter'].sudo().get_param('attachement_restriction.require_attachment')
        print(mandatory)

        if mandatory == "True":
            print("mandatory")
            for rec in self:
               print(rec)
               attachment=self.env['ir.attachment'].search([
                   ('res_model','=', 'purchase.order'),
                   ('res_id','=', rec.id),
                   ('mimetype','in',['application/pdf','image/png','image/jpeg']),
                   # ('mimetype','=','image/JPG'),
                   # ('mimetype', '=', 'image/PNG')

               ])
               print(len(attachment))
               if not attachment:
                   raise ValidationError("Purchase Order can not be created")

        return super().button_confirm()




