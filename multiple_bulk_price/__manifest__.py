{
    'name': 'Multiple bulk price',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "multiple bulk price",
    'sequence': -10,
    'summary': "Multiple mulk price",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["sale","mail", "contacts",'account','product','fleet'],
    'data': [
        "security/ir.model.access.csv",
        "security/user_groups.xml",
        "wizards/bulk_wizard.xml",
        "views/sale_order.xml",
             ]
}