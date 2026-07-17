from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    allowed_customer_tag_ids = fields.Many2many("res.partner.category",compute="_compute_allowed_customer_tag")



    @api.depends("company_id")

    def _compute_allowed_customer_tag(self):
        for rec in self:

            rec.allowed_customer_tag_ids=rec.company_id.customer_tag_ids
