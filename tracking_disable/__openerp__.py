# -*- coding: utf-8 -*-
{
    'name': "tracking_disable",
    'summary': """
        Automatically disable followers when creating. """,
    'description': """
        Automatically disable followers when creating.
    """,
    'author': "bisneSmart",
    'website': "http://www.bisnesmart.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Mail',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'account',
                ],
    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
