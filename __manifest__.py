# -*- coding: utf-8 -*-
{
    'name': "prod_serv",

    'summary': """
        Module that adds the column Bien/Servicio
        To identify the type of product of invoices or Vendor Bills""",

    'description': """
        Module that adds the column Bien/Servicio
        To identify the type of product of invoices or Vendor Bills,
        and then apply this to a Custom Financial Report
    """,

    'author': "Avalantec",
    'website': "https://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_move.xml',
        'views/account_move_line.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
