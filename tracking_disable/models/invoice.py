# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#   Copyright (C) 2016 bisneSmart
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import api, exceptions, fields, models, _

class AccountInvoice(models.Model):
    """
    Deshabilitar el seguimiento automático y envío de email al crear
    """
    _inherit = 'account.invoice'
    @api.model
    def create(self,data):
        return super(AccountInvoice,self.with_context(
                                                        tracking_disable=True
                                                        )).create(data)
