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

{'name': 'Project Assignment',
 'version': '1.0',
 'category': 'Project',
 'depends': ['base_recursive_model',
             'project',
             ],
 'author': 'Yannick Buron',
 'license': 'AGPL-3',
 'website': 'https://launchpad.net/',
 'description': """
Project Assignment
=================
""",
 'demo': ['data/project_assignment_demo.xml'],
 'data': ['security/ir.model.access.csv',
          'project_assignment_view.xml'],
 'test': ['tests/project_assignment_test.yml'],
 'installable': True,
 'application': True,
}
