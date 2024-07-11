# -*- encoding: utf-8 -*-

{
    'name': 'OWL Custom',
    'author': "GM",
    'sequence': 1,
    'version': '16.0.1.0',
    'summary': "OWL Custom Features",
    'description': """ OWL Custom Features """,
    "license" : "OPL-1",
    'depends': ['base', 'point_of_sale'],
    'data': [
        "security/ir.model.access.csv",
        "views/todo_list_views.xml",
    ],

    "assets": {
        "point_of_sale.assets": [
            "owl_custom/static/src/components/pos/*/*.js",
            "owl_custom/static/src/components/pos/*/*.xml",
        ],
        "web.assets_backend": [
            "owl_custom/static/src/components/todo_list/*/*.js",
            "owl_custom/static/src/components/todo_list/*/*.xml",
            "owl_custom/static/src/components/todo_list/*/*.scss",
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
