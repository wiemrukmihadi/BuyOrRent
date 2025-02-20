from odoo import models, fields

class Car(models.Model):
    _name = 'vehicle.car'
    _inherit = 'vehicle'
    _description = 'Car'

    car_type = fields.Selection([
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('convertible', 'Convertible'),
        ('pickup', 'Pickup')
    ], string="Car Type")
