from odoo import models, fields

class Truck(models.Model):
    _name = 'vehicle.truck'
    _inherit = 'vehicle'
    _description = 'Truck'

    truck_capacity = fields.Float(string="Capacity (Tons)")
    axle_count = fields.Integer(string="Axle Count")
