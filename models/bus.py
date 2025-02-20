from odoo import models, fields

class Bus(models.Model):
    _name = 'vehicle.bus'
    _inherit = 'vehicle'
    _description = 'Bus'

    seat_capacity = fields.Integer(string="Seat Capacity")
    bus_type = fields.Selection([
        ('city', 'City Bus'),
        ('intercity', 'Intercity Bus'),
        ('school', 'School Bus')
    ], string="Bus Type")
