from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'hr.employee'


    is_available_technician = fields.Boolean(string="Is Available Technician")