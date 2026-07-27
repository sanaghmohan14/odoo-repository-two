{
    'name': 'Product Price Restrict',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "PRODUCT",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale'],
    'data': [
                "views/product_template.xml"
           ]
}