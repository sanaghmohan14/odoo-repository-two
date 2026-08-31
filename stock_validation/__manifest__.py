{
    'name': 'Stock Validation',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "stock",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','stock','contacts','product'],
    'data': [

            "views/res_partner.xml"
           ]
}