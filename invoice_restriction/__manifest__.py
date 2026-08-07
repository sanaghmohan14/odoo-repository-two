{
    'name': 'Invoice restriction ',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "invoice restriction",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale'],
    'data': [
        "views/account_move.xml",
                "views/res_partner.xml"
           ]
}