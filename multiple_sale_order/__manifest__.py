{
    'name': 'Multiple Sale Order',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "Sales Management",
    'sequence': -10,
    'summary': "Multiple Sale Order Management",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["sale","mail", "contacts",'account','product','fleet'],
    'data': ["views/account_move_views.xml",
        # "views/sale_order_views.xml",
             ]
}