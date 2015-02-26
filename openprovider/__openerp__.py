# -*- coding: utf-8 -*-
{
    'name': "openprovider",

    'summary': """
        Openprovider integration""",

    'description': """
        Openprovider integration with Odoo
    """,

    'author': "Royendgel Silberie",
    'website': "https://github.com/royendgel/odoo_openprovider",

    'category': 'Extra Tools',
    'version': '0.2',


    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}