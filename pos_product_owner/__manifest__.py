{
    'name': 'Pos Product Owner',
    'version': '19.0.1.1.1',
    'author': "cybrosys",
    'sequence': -10,
    'summary': "PRODUCT OWNER",
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','mail','product','sale','point_of_sale','pos_restaurant'],
    'data': [
                "views/product_template.xml"
           ],

    'assets':{
        'point_of_sale._assets_pos':
            [

             "pos_product_owner/static/src/xml/pos_field.xml",
                # "pos_product_owner/static/src/xml/pos_card.xml",
                # "pos_product_owner/static/src/js/pos_edit.js",
                # "pos_product_owner/static/src/xml/pos_receipt.xml",


            ]
    }
}