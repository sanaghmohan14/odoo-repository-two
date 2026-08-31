{
    'name': 'Remove Order Line',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "Remove Orders",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','stock','point_of_sale','pos_restaurant'],
    'data': [
        "views/res_partner.xml"

           ],
    'assets': {
        'point_of_sale._assets_pos':
            [
                "remove_order_pos/static/src/js/payment_validation.js",
                "remove_order_pos/static/src/xml/screen_button.xml",
                # "remove_order_pos/static/src/xml/top_button.xml",
                "remove_order_pos/static/src/js/remove_button.js",
                "remove_order_pos/static/src/xml/remove_button.xml",
                "remove_order_pos/static/src/xml/add_button.xml",
        ]
    }
}