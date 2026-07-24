{
    'name': 'project Restrict',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "CRM",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','crm','mail','project','hr'],
    'data': [
        # "views/project_project.xml",
        "views/res_users.xml",
                "views/hr_employee.xml",
           ]
}