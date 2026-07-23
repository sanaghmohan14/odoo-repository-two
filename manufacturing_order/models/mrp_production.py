from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MrpProductionExt(models.Model):
    _name = "mrp.production.ext"
    _description = "Production Order"

    name = fields.Char(default="New")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    bom_id = fields.Many2one("mrp.bom", string="Bom")
    quantity = fields.Float(string="Quantity", default=1, required=True)
    planned_date = fields.Datetime(string="Planned Date", required=True)

    state = fields.Selection(
        [("draft", "draft"), ('confirmed', 'confirmed'), ("inprogress", "inprogress"), ("done", "done"),
         ('cancelled', 'cancelled')], default="draft")

    material_line_ids = fields.One2many("mrp.production.material", "production_id", string="materials", )
    is_material_available = fields.Boolean(compute="_compute_material_available", store=True,
                                           string="material available")

    # material_count=fields.Integer(compute="_compute_material_count",store=True, string="Materials")

    total_consumed = fields.Float(compute="_compute_total", store=True, string="Total consumed")

    remaining_materials = fields.Float(string="")

    produced_qty = fields.Float(string="produced qty")

    # repair_count= fields.Integer(string="Repair count",compute="_compute_material_count",store=True)

    material_history = fields.Char(action="action_view_material")

    consume_material = fields.Char(string="Consume Material", action="action_consume_material")

    material_counts = fields.Integer(string="Material Counts", compute="compute_material_count")

    @api.model
    def create(self, vals_list):
        """create function is used to create the reference/ sequence id when creating a  new repair service """
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('mrp.production.ext') or 'New'
            return super().create(vals_list)

    @api.onchange("bom_id")
    def _onchange_bom_id(self):
        """load material lines from bom"""
        self._load_material_lines()

    @api.onchange("bom_id")
    def _onchange_bom(self):
        if self.bom_id:
            self.product_id = self.bom_id.product_id

    @api.onchange("quantity")
    def _onchange_quantity(self):
        """load matrials quantity based on quantity"""
        self._load_material_lines()

    # @api.onchange("bom_id")
    # def _onchange_bom_id_one(self):
    #     self.bom_id.

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

    # def action_confirm(self):
    #     if not self.bom_id:
    #         raise ValidationError("Please select a bill of material")
    #     if not self.product_id:
    #         raise ValidationError("Please select a product")
    #     self.state = "confirmed"



    # material avai
    @api.depends("material_line_ids.required_qty", "material_line_ids.available_qty")
    def _compute_material_available(self):
        for rec in self:
            rec.is_material_available = all(line.available_qty >= line.required_qty for line in rec.material_line_ids)

    # def action_done(self):
    #     self.state = "done"
    #
    #
    # def action_confirm_production(self):
    #     self.state = "confirmed"
    #
    #
    # def action_start_production(self):
    #     self.state = "inprogress"

    # material count

    def compute_material_count(self):
        for rec in self:
            rec.material_counts = len(rec.material_line_ids)
            # rec.material_count = self.env['vechicle.service'].search_count([('partner_id', '=', rec.partner_id.id)])

    # total consumed

    @api.depends("material_line_ids.required_qty", "material_line_ids.consumed_qty")
    def _compute_total(self):
        for rec in self:
            rec.total_consumed = sum(rec.material_line_ids.mapped("consumed_qty"))

            rec.remaining_materials = sum(line.required_qty - line.consumed_qty for line in rec.material_line_ids)

    # confirm production
    def action_confirm(self):
        for rec in self:
            if not rec.bom_id:
                raise ValidationError("Please select a bill of material")
            if rec.quantity <= 0:
                raise ValidationError("please select a quantity")
            if not rec.product_id.is_manufacturable:
                raise ValidationError("Please select a manufacturable product")
            rec.state = "confirmed"

    # start production
    def action_start(self):
        print("1")
        for rec in self:
            if not rec.is_material_available:
                raise ValidationError("materials are not avaialable")
            rec.state = "inprogress"

    # consume material

    def action_consume_material(self):
        for rec in self:
            for line in rec.material_line_ids:
                if line.consumed_qty > line.required_qty:
                    raise ValidationError("consmed qty cannot exceed required qty")
                line.consumed_qty = line.required_qty

    # view materias
    def action_view_material(self):
        print("hi")
        return {
            "type": "ir.actions.act_window",
            "name": "materials",
            "res_model": "mrp.production.material",
            "view_mode": "list,form",
            "domain": [("production_id", "=", self.id)],

        }

    def action_cancel(self):
        self.state = "cancelled"

        # mark done

    def action_done(self):
        for rec in self:
            for line in rec.material_line_ids:
                # if line.consumed_qty<line.required_qty:
                #     raise ValidationError("required qty must")
                if not rec.material_line_ids:
                    raise ValidationError("material lines must not be empty")
            rec.state = "done"
