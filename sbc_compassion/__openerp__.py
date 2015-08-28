# -*- coding: utf-8 -*-
##############################################################################
#
#       ______ Releasing children from poverty      _
#      / ____/___  ____ ___  ____  ____ ___________(_)___  ____
#     / /   / __ \/ __ `__ \/ __ \/ __ `/ ___/ ___/ / __ \/ __ \
#    / /___/ /_/ / / / / / / /_/ / /_/ (__  |__  ) / /_/ / / / /
#    \____/\____/_/ /_/ /_/ .___/\__,_/____/____/_/\____/_/ /_/
#                        /_/
#                            in Jesus' name
#
#    Copyright (C) 2014-2015 Compassion CH (http://www.compassion.ch)
#    @author: Emmanuel Mathier <emmanuel.mathier@gmail.com>
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

{
    'name': "Sponsor to beneficiary communication",
    'version': '0.1',
    'category': 'sbc',
    'summary': """
        SBC - Sponsor to beneficiary communication""",
    'sequence': 150,
    'author': 'Compassion CH',
    'website': 'http://www.compassion.ch',
    'description': """
        The sbc.compassion module can handle the different interactions of
        correspondence between sponsors and their children sponsorships
    """,
    'depends': ['base', 'base_location', 'sponsorship_compassion'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        'view/country_compassion_view.xml',
        'view/partner_compassion_view.xml',
        'view/lang_compassion_view.xml',
        'data/lang_data.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}