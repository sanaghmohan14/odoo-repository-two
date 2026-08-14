{
    'name': 'Internal Notes',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': "Internal Notes",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'account','product','sale','mrp'],
    'data': [

                "views/deliver_slip.xml",
                "views/stock_picking.xml"

     ]

}
