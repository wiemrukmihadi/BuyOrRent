{
    'name': 'BuyOrRent',
    'version': '1.0',
    'category': 'Buy Or Rent Car',
    'author': '@phaalawnbreotpneg',
    'website': 'https://buyorrent.com',
    'summary': 'Manage Buy or Rent Car',
    'depends': ['base'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/vehicle_view.xml',
        'views/vehicle_image_view.xml',
        'views/vehicle_manufacturer.xml',
        'views/car_view.xml',
        'views/truck_view.xml',
        'views/bus_view.xml',
        'views/motorcycle_view.xml',
        'views/menu.xml',
    ],
    'demo': [
        # 'demo/demo.xml',  # Add this line for demo data
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
