{
    'name': 'delivery hold',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "CRM",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'crm','sale'],
    'data': [
        "views/sale_order.xml"

    ]
}