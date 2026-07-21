{
    'name': 'Attendance List',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'category': "Attendance List",
    'sequence': -10,
    'summary': "Attendance list Management",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','hr','mail','hr_attendance','product',"sale", "contacts",],
    'data': [
        "security/ir.model.access.csv",
        "views/sale_order.xml",
        "views/bulk_price_update.xml",
        "views/day_wise_attendance_views.xml",
        "views/day_wise_attendence_menu.xml",
             ]
}