{
    'name': 'Tag Filtering',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Tag filtering for customer and vendor",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','sale','purchase'],
    'data': [
        "views/res_config_views.xml",
        "views/purchase_order_views.xml",
        "views/sale_order_views.xml"

           ]
}