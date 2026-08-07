{
    'name': 'Customer Invoice Hold',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "invoice hold",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale'],
    'data': [
                "security/ir.model.access.csv",
                "views/res_partner.xml",
                "views/customer_invoice_hold.xml",
                "views/invoice_restrict_menu.xml"
           ]
}