# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrPayslipCst(models.Model):
    _inherit = 'hr.payslip'
    
    def _create_account_move(self, values):
        partner_id = self.employee_id.user_id.partner_id.id if self.employee_id and self.employee_id.user_id and self.employee_id.user_id.partner_id else None 
        values['employee_partner_id'] = partner_id
        return super(HrPayslipCst, self)._create_account_move(values)


class AccountMove(models.Model):
    _inherit = 'account.move'

    employee_partner_id = fields.Many2one('res.partner',
        check_company=True,
        string='Partner', ondelete='restrict')