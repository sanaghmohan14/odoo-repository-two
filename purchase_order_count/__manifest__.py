{
    'name': 'Order restriction',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': "order restriction",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'account','product','fleet','purchase'],
    'data': [

"views/purchase_order_views.xml"

     ]

}
