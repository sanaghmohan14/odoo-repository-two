{
    'name': 'Sale Order Merge',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': "Sale Merging",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'product','sale'],
    'data': [
                    "security/ir.model.access.csv",
                    "wizards/merge_wizard.xml",
                "views/sale_order.xml"

     ]

}
