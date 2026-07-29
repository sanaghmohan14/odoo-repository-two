from odoo import api, fields, models



class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'




    # @api.model
    # def _hide_menus(self)





    # def _visible_menu_ids(self,debug=False):
    #     menus=super()._visible_menu_ids(debug)
    #     hidden=self.env.user.menu_ids.ids
    #     visible=menus-hidden
    #     return visible




    def _filter_visible_menus(self):
        menus = super()._filter_visible_menus()
        hidden=self.env.user.menus_ids.ids
        if hidden:
            menus=menus.filtered(lambda m: m.id not in hidden)
        return menus
