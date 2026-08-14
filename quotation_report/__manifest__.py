{
    'name': 'Quotation Report',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': "Quotation Report",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'account','product','sale','mrp'],
    'data': [

                "views/sale_order.xml"

     ]

}
