from odoo import models, fields

class Motorcycle(models.Model):
    _name = 'vehicle.motorcycle'
    _inherit = 'vehicle'
    _description = 'Motorcycle'

    engine_capacity = fields.Float(string="Engine Capacity (CC)")
    type_motor = fields.Selection([
        ('sport', 'Sport'),
        ('naked', 'Naked'),
        ('scooter', 'Scooter'),
        ('cruiser', 'Cruiser')
    ], string="Motorcycle Type")
