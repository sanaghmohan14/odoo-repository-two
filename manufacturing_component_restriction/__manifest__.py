{
    'name': 'Mrp Restriction',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "mrp production restriction",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale','mrp'],
    'data': [

        "security/ir.model.access.csv",
        "views/product_template.xml",
        "wizards/mrp_wizard.xml",
      "views/mrp_production.xml",

           ]
}