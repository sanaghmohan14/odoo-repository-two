from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MrpProductionExt(models.Model):
    _name = "mrp.production.ext"
    _description = "Production Order"

    name = fields.Char(default="New")
    product_id = fields.Many2one("product.product", string="Product",required=True)
    bom_id = fields.Many2one("mrp.bom", string="BoM",required=True)
    quantity = fields.Float(string="Quantity", default=1,required=True)
    planned_date = fields.Datetime(string="Planned Date",required=True)

    state = fields.Selection([("draft","draft"),('confirmed','confirmed'),("inprogress", "inprogress"),("done","done"),('cancelled','cancelled')], default="draft")

    material_line_ids = fields.One2many("mrp.production.material","production_id",string="materials",)
    is_material_available = fields.Boolean(compute="_compute_material_available",store=True, string="material available")





    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('mrp.production.ext') or 'New'
            return super().create(vals_list)


    @api.onchange("product_id")
    def _onchange_product_id(self):
        """on change when product is changed"""
        if self.product_id:
            bom = self.env["mrp.bom"].search([("product_tmpl_id", "=", self.product_id.product_tmpl_id.id)], limit=1)
            self.bom_id = bom


    @api.onchange("bom_id")
    def _onchange_bom_id(self):
        """load material lines from bom"""
        self._load_material_lines()


    @api.onchange("quantity")
    def _onchange_quantity(self):
        self._load_material_lines()



    def _load_material_lines(self):
        x = [fields.Command.clear()]
        if not self.bom_id:
            return {
                "warning": {
                    "title": "Warning",
                    "message": "plese select a bill of material"
                }
            }
        for line in self.bom_id.bom_line_ids:
            x.append(
                fields.Command.create({
                    "product_id": line.product_id.id,
                    "required_qty": line.product_qty * self.quantity,
                })
            )
        self.material_line_ids = x


    def action_confirm(self):
        if not self.bom_id:
            raise ValidationError("Please select a bill of material")
        if not self.product_id:
            raise ValidationError("Please select a product")
        self.state = "confirmed"

    def action_start(self):
        print("hi")


    @api.depends("material_line_ids.required_qty", "material_line_ids.available_qty")
    def _compute_material_available(self):
        for rec in self:
            rec.is_material_available = all(
                line.available_qty >= line.required_qty
                for line in rec.material_line_ids
            )



    def action_done(self):
        self.state = "done"


    def action_confirm_production(self):
        self.state = "confirmed"


    def action_start_production(self):
        self.state = "inprogress"






















