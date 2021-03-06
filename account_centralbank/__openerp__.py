# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Buron
#    Copyright 2013 Yannick Buron
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

{'name': 'Account CentralBank',
 'version': '1.0',
 'category': 'Association',
 'depends': ['base_community',
             'account_accountant',
             'account_reversal',
             ],
 'author': 'Yannick Buron',
 'license': 'AGPL-3',
 'website': 'https://launchpad.net/marketplace',
 'description': """
Account CentralBank
=================

""",
 'demo': ['data/account_centralbank_demo.xml'],
 'data': ['security/account_centralbank_security.xml',
          'account_centralbank_view.xml',
          'account_centralbank_data.xml',
          'account_centralbank_workflow.xml',
          'res_config_view.xml',
          'security/ir.model.access.csv'
          ],
 'test': ['tests/account_centralbank_users.yml',
          'tests/account_centralbank_rights.yml',
          'tests/account_centralbank_moderator.yml',
          'tests/account_centralbank_external.yml',
          'tests/account_centralbank_limits.yml',
          'tests/account_centralbank_balances.yml',
          ],
 'installable': True,
 'application': True,
}
