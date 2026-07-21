{
    'name': 'mrp production',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "mrp production",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'fleet', "mail", "contacts", 'account', 'product','mrp','hr'],
    'data': [
        "security/ir.model.access.csv",
        "data/reference.xml",
        "views/mrp_production_material_views.xml",
        "views/mrp_production_views.xml",
        "views/mrp_menu.xml",

    ]
}