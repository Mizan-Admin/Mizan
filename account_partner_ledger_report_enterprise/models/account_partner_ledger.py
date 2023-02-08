from odoo import fields, models, api

class ReportPartnerLedgerCustom(models.AbstractModel):
    _inherit = 'account.partner.ledger'

    def _get_columns_name(self, options):
        res = super(ReportPartnerLedgerCustom, self)._get_columns_name(options)
        for i in res:
            if i.get('name') == 'JRNL':
                res[res.index(i)] = {}
            if i.get('name') == 'Account':
                res[res.index(i)] = {}
            if i.get('name') == 'Matching Number':
                res[res.index(i)] = {}
            if i.get('name') == 'Amount Currency':
                res[res.index(i)] = {}
        return res

    def _get_report_line_move_line(self, options, partner, aml, cumulated_init_balance, cumulated_balance):
        res = super(ReportPartnerLedgerCustom, self)._get_report_line_move_line(options, partner, aml, cumulated_init_balance, cumulated_balance)
        if res.get('columns'):
            res.get('columns')[0] = {'name': ''}
            res.get('columns')[1] = {'name': ''}
            res.get('columns')[4] = {'name': ''}
            if self.user_has_groups('base.group_multi_currency'):
                res.get('columns')[8] = {'name': ''}
        return res