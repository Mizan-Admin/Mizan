# -*- coding: utf-8 -*-
{
    'name': "Employee PaySlip",
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'depends': [
         'documents_hr_payroll', 'hr_payroll_account',
    ],
    'data': [
        'views/account_move.xml',
    ],
    'application': True,
}
