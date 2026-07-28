from odoo import api, fields, models



class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'





    @api.model
    def hide_menu(self):
        for menu in self:
            print("one")
            menus=self.env['ir.ui.menu'].search([('id','=',menu.id)])
            hidden_menu
