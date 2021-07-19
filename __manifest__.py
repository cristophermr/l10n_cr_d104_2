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
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_line.xml',
        'data/account.financial.html.report.csv',
        'data/account.financial.html.report.line.csv',
        'data/account.analytic.tag.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
