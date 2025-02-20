from odoo import api, SUPERUSER_ID

def create_default_manufacturers(env):
    manufacturers = [
        {'name': 'Toyota', 'country': 'Japan', 'established_year': 1937},
        {'name': 'Honda', 'country': 'Japan', 'established_year': 1948},
        {'name': 'Ford', 'country': 'USA', 'established_year': 1903},
        {'name': 'Tesla', 'country': 'USA', 'established_year': 2003},
        {'name': 'BMW', 'country': 'Germany', 'established_year': 1916},
        {'name': 'Mercedes-Benz', 'country': 'Germany', 'established_year': 1926},
        {'name': 'Hyundai', 'country': 'South Korea', 'established_year': 1967},
        {'name': 'Ducati', 'country': 'Italy', 'established_year': 1926},
        {'name': 'Yamaha', 'country': 'Japan', 'established_year': 1955},
        {'name': 'Harley-Davidson', 'country': 'USA', 'established_year': 1903}
    ]

    for manufacturer in manufacturers:
        env['vehicle.manufacturer'].create(manufacturer)

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    create_default_manufacturers(env)
