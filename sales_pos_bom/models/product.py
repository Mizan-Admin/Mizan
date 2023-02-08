# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    so_pos_uom_id = fields.Many2one('uom.uom', string='SO POS Unit of Measure')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    so_pos_uom_id = fields.Many2one('uom.uom', string='SO POS Unit of Measure',related="product_id.product_tmpl_id.so_pos_uom_id")


class POSOrderLine(models.Model):
    _inherit = 'pos.order.line'

    so_pos_uom_id = fields.Many2one('uom.uom', string='SO POS Unit of Measure',related="product_id.product_tmpl_id.so_pos_uom_id")
