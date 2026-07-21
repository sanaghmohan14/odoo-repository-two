{
    'name': 'fleet model new',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "fleet model configuration",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','fleet',"mail", "contacts",'account','product'],
    'data': [
        # "security/ir.model.access.csv",
        
        "views/hr_employee_views.xml",

        "views/feet_vehicle.xml",

        "data/reference.xml",

        "views/fleet_service_order_checklist_views.xml",

        "views/fleet_service_order_part.xml",

        "views/fleet_service_order.xml",

        "views/fleet_service_menu.xml"
           ]
}