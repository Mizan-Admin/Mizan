# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrderLineCst(models.Model):
    _inherit = 'purchase.order.line'
    
    _sql_constraints = [
        ('accountable_required_fields',
            "CHECK(display_type IS NOT NULL)",
            "Missing required fields on accountable purchase order line."),
        ('non_accountable_null_fields',
            "CHECK(display_type IS NULL)",
            "Forbidden values on non-accountable purchase order line"),
    ]


class SaleOrderLineCst(models.Model):
    _inherit = 'sale.order.line'

    _sql_constraints = [
        ('accountable_required_fields',
            "CHECK(display_type IS NOT NULL)",
            "Missing required fields on accountable sale order line."),
        ('non_accountable_null_fields',
            "CHECK(display_type IS NULL)",
            "Forbidden values on non-accountable sale order line"),
    ]
