{
    'name': 'MAndatory Attachment',
    'version': '19.0.1.1',
    'author': "cybrosys",
    'category': "service",
    'sequence': -10,
    'summary': " Attachment",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ["mail", "contacts",'account','product','fleet','purchase','sale'],
    'data': [

            "views/res_config_settings.xml"
     ]

}
