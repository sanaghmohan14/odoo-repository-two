{
    'name': 'Machines',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Machines",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base', "mail", "contacts", 'product','hr'],
    'data': [
                "security/ir.model.access.csv",
                "data/reference.xml",
                "views/machine_tools.xml",
                "views/machine_uses.xml",
                "views/machine_menu.xml"

    ]
}