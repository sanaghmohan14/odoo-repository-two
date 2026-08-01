{
    'name': 'employee Loan',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "employee loan",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'fleet', "mail", "contacts", 'account', 'product','mrp','hr'],
    'data': [
        "security/ir.model.access.csv",
        "data/reference.xml",
        "views/employee_loan_line.xml",
        "views/employee_loan.xml",
        "views/employee_loan_menu.xml"

    ]
}