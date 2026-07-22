{
    'name': 'Bulk Price',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Bulk Price",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base', "mail", "contacts", 'account', 'product'],
    'data': [
        "views/sale_order.xml",
"views/bulk_price_update.xml",
"views/bulk_price_menu.xml",
    ]
}