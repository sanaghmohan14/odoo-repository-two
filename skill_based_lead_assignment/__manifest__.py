{
    'name': 'Lead Assignment',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Lead Assignment For Sales Team",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm'],
    'data': [
        "views/res_users_views.xml",
        # "views/crm_lead_views.xml",
           ]
}