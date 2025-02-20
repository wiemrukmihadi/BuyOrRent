from odoo import models, fields

class VehicleImage(models.Model):
    _name = 'vehicle.image'
    _description = 'Vehicle Image'

    name = fields.Char(string="Image Name")
    image = fields.Binary(string="Image", required=True)
    vehicle_id = fields.Many2one('vehicle', string="Vehicle", required=True, ondelete='cascade')
