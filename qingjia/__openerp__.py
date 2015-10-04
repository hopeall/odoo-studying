# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

{
    'name': 'qingjia_leave',
    'version': '1.0',
    'category': 'Project Management',
    'sequence': 9,
    'summary': '请假模块，提供请假功能',
    'description': """
提供请假功能
    """,
    'author': 'yue.yang',
    'website': 'http://shine-it.net/index.php/topic,882.0.html',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'workflow/tiaoxiu_workflow.xml',
        'views/qingjia_view.xml',
     ],
    'demo': ['data/demo.xml'],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
