{
    'name': 'Product Price Change',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "PRODUCT PRICE CHANGE",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale'],
    'data': [
        "security/ir.model.access.csv",
                "wizards/price_wizard.xml",
                "views/product_template.xml",
        "views/product_service_history.xml",
        "views/product_service_menu.xml"
           ]
}