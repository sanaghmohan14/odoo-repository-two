{
    'name': 'Max Stock Validation',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Stock validation based on quantity",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','stock'],
    'data': ["views/stock_location_views.xml",
             "views/stock_picking_views.xml"


           ]
}