{
    'name': 'Revision Tracking',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "REVISION TRACKING",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','product','sale'],
    'data': [
        "security/ir.model.access.csv",
        "data/reference.xml",
        "views/sale_order.xml",
        "views/revision_tracking.xml",
                "views/revision_tracking_menu.xml"
           ]
}