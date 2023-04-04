# -*- coding: utf-8 -*-
{
    'name': "CR Reporte Hacienda D104",

    'summary': """
        To identify the type of product of
        invoices or Vendor Bills as Bien/Servicio using the Analytic Tags""",

    'description': """
        To identify the type of product of
        invoices or Vendor Bills as Bien/Servicio using the Analytic Tags,
        and then apply this to a Custom Financial Report
    """,

    'author': "Avalantec",
    'website': "https://www.avalantec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant','sale_management'],

    # always loaded
    'data': [
        'views/account_move_line.xml',
        'data/account.report.csv',
        'data/account.account.tag.csv',
        #'data/account.report.line.csv',
    ],
}
