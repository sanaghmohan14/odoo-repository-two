{
    'name': 'Sale Order Tree',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': "Sale Order Tree",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'product','sale'],
    'data': [

        "views/product_product.xml",
                "views/sale_order.xml",
        "views/res_partner.xml"

     ]

}
