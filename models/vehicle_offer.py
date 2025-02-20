from odoo import models, fields

class VehicleOffer(models.Model):
    _name = 'vehicle.offer'
    _description = 'Vehicle Offer'

    vehicle_id = fields.Many2one('vehicle', string="Vehicle", required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    offer_type = fields.Selection([('buy', 'Buy'), ('rent', 'Rent')], string="Offer Type", required=True)
    offer_price = fields.Float(string="Offer Price", required=True)
    rental_days = fields.Integer(string="Rental Days")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], string="Status", default='pending')

    def action_accept(self):
        for offer in self:
            offer.status = 'accepted'
            offer.vehicle_id.state = 'sold' if offer.offer_type == 'buy' else 'rented'

    def action_reject(self):
        for offer in self:
            offer.status = 'rejected'
