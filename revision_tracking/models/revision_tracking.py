from datetime import datetime, timedelta
from odoo import fields,models,api
from odoo.exceptions import ValidationError
from odoo.orm.decorators import ondelete


class RevisionTracking(models.Model):
    _name="revision.tracking"
    _rec_name = "sale_id"


    sale_id = fields.Many2one('sale.order')

    sale_order_id = fields.Many2one('sale.order.line')

    name = fields.Char(string='Revision No.', readonly=True ,default='New')
    modified_by=fields.Many2one('res.users',string="Revision Owner")
    modified_on=fields.Datetime(string="Revision Date")
    revision_notes=fields.Text(string="Revision Notes")







    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('revision.tracking') or 'New'
            return super().create(vals_list)


