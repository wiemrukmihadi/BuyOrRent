from odoo import models, fields

class VehicleManufacturer(models.Model):
    _name = 'vehicle.manufacturer'
    _description = 'Vehicle Manufacturer'

    name = fields.Char(string="Manufacturer Name", required=True)
    country = fields.Char(string="Country of Origin")
    established_year = fields.Integer(string="Established Year")
    logo = fields.Binary(string="Logo")
    vehicle_ids = fields.One2many('vehicle', 'manufacturer_id', string="Vehicles")

    _sql_constraints = [
        ('unique_manufacturer_name', 'UNIQUE(name)', 'Manufacturer name must be unique!')
    ]
