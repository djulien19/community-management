# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import netsvc
from openerp import pooler
from openerp import SUPERUSER_ID
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp

import logging
#_logger = logging.getLogger(__name__)


class vote_type(osv.osv):
    _name = 'vote.type'

    _columns = {
        'name': fields.char('Name', size=128, required=True),
    }


class community_config_settings(osv.osv):
    _inherit = 'community.config.settings'

    _columns = {
        'vote_line_ids': fields.one2many('vote.config.line', 'res_id',
            domain=lambda self: [('model', '=', self._name)],
            auto_join=True,
            string='Lines'),
    }


    def write(self, cr, uid, ids, vals, context=None):
        res = super(community_config_settings, self).write(cr, uid, ids, vals, context=context)

        models = {}
        for config in self.browse(cr, uid, ids, context=context):
            for line in config.vote_line_ids:
                models[line.target_model.model] = line.target_model.model

        for model in models:
            model_obj = self.pool.get(model)
            model_ids = model_obj.search(cr, uid, [('parent_id', '=', False)], context=context)
            model_obj._update_stored_config(cr, uid, model_ids, context=context)
        return res



class vote_config_line(osv.osv):
    _name = 'vote.config.line'

    _inherit = 'base.config.inherit.line'

    _columns = {
        'target_model': fields.many2one('ir.model', 'Target model', ondelete='cascade'),
        'name': fields.many2one('vote.type', 'Name', required=True),
    }

    _order = 'target_model, sequence'


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
