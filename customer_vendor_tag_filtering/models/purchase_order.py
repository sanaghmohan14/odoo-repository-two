from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Many2one('res.partner')

    allowed_vendor_tag_ids = fields.Many2many("res.partner.category", compute="_compute_allowed_vendor_tag")

    @api.depends("company_id")

    def _compute_allowed_vendor_tag(self):
        for rec in self:
            rec.allowed_vendor_tag_ids = rec.company_id.vendor_tag_ids


