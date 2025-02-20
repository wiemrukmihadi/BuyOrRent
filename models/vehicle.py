from odoo import models, fields

class Vehicle(models.Model):
    _name = 'vehicle'
    _description = 'Vehicle Base Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Vehicle Name", required=True, tracking=True)
    manufacturer_id = fields.Many2one('vehicle.manufacturer', string="Manufacturer", required=True)
    image_ids = fields.One2many('vehicle.image', 'vehicle_id', string="Vehicle Images")
    offer_ids = fields.One2many('vehicle.offer', 'vehicle_id', string="Offers")
    type = fields.Selection([
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('motorcycle', 'Motorcycle')
    ], string="Vehicle Type", required=True, tracking=True)
    
    condition = fields.Selection([
        ('new', 'New'),
        ('used', 'Used')
    ], string="Condition", required=True, tracking=True, default='used')

    availability = fields.Selection([
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('both', 'For Sale & Rent')
    ], string="Availability", required=True, default='sale')

    brand = fields.Char(string="Brand", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Integer(string="Year", required=True)
    price = fields.Float(string="Selling Price", required=True)
    rent_price_per_day = fields.Float(string="Rent Price per Day", help="Only applicable if vehicle is for rent")

    mileage = fields.Integer(string="Mileage (KM)")
    fuel_type = fields.Selection([
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid')
    ], string="Fuel Type")

    transmission = fields.Selection([
        ('manual', 'Manual'),
        ('automatic', 'Automatic')
    ], string="Transmission")

    engine_number = fields.Char(string="Engine Number", required=True, unique=True)
    license_plate = fields.Char(string="License Plate", required=True, unique=True)

    seller_id = fields.Many2one('res.partner', string="Seller", required=True)
    buyer_id = fields.Many2one('res.partner', string="Buyer")

    status = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('canceled', 'Canceled')
    ], string="Status", default="available")

    color = fields.Integer(string="Color", help="Vehicle Color (Odoo Color Index)")

    _sql_constraints = [
        ('unique_engine_number', 'UNIQUE(engine_number)', 'Engine Number must be unique!'),
        ('unique_license_plate', 'UNIQUE(license_plate)', 'License Plate must be unique!')
    ]
