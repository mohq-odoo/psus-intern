# -*- coding: utf-8 -*-

{
    'name': 'AutoCancelQuotations',

    'summary': 'A module to delete expired quotations each day at midnight',

    'description': 'A module to delete expired quotations each day at midnight - yall',

    'author': 'OdooPS',

    'category': 'sales',

    'version': '15.0.1.0.0',

    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'tvu_networks/views/auto_cancel_quotations.xml'
    ],
    'demo': [
    ],    

    'license': 'OPL-1'
}
