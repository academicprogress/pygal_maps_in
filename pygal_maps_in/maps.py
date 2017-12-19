# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Indian districts and staes maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from pygal._compat import u
from numbers import Number
import os

'''
https://en.wikipedia.org/wiki/List_of_districts_in_India
'''

DISTRICTS = {
    'AN-NI': u("Nicobar"),
    'AN-NA': u("North and Middle Andaman"),
    'AN-SA': u("South Andaman"),
    'AP-AN': u("Anantapur"),
    '05': u(""),
    '06': u(""),
    'AR-AJ': u(""),
    '08': u(""),
    '09': u(""),
    '10': u(""),
    'AS-BK': u(""),
    '12': u(""),
    '13': u(""),
    '14': u(""),
    '15': u(""),
    '16': u(""),
    '17': u(""),
    '18': u(""),
    '19': u(""),
    '2A': u(""),
    '2B': u(""),
    '21': u(""),
    '22': u(""),
    '23': u(""),
    '24': u(""),
    '25': u(""),
    '26': u(""),
    '27': u(""),
    '28': u(""),
    '29': u(""),
    '31': u(""),
    '30': u(""),
    '32': u(""),
    '34': u(""),
    '33': u(""),
    '35': u(""),
    '36': u(""),
    '37': u(""),
    '38': u(""),
    '39': u(""),
    '40': u(""),
    '41': u(""),
    '42': u(""),
    '43': u(""),
    '44': u(""),
    '45': u(""),
    '46': u(""),
    '47': u(""),
    '48': u(""),
    '49': u(""),
    '50': u(""),
    '51': u(""),
    '52': u(""),
    '53': u(""),
    '54': u(""),
    '55': u(""),
    '56': u(""),
    '57': u(""),
    '58': u(""),
    '59': u(""),
    '60': u(""),
    '61': u(""),
    '62': u(""),
    '63': u(""),
    '64': u(""),
    '65': u(""),
    '66': u(""),
    '67': u(""),
    '68': u(""),
    '69': u(""),
    '70': u(""),
    '71': u(""),
    '72': u(""),
    '73': u(""),
    '74': u(""),
    '75': u(""),
    '76': u(""),
    '77': u(""),
    '78': u(""),
    '79': u(""),
    '80': u(""),
    '81': u(""),
    '82': u(""),
    '83': u(""),
    '84': u(""),
    '85': u(""),
    '86': u(""),
    '87': u(""),
    '88': u(""),
    '89': u(""),
    '90': u(""),
    '91': u(""),
    '92': u(""),
    '93': u(""),
    '94': u(""),
    '95': u(""),
    '971': u(""),
    '972': u(""),
    '973': u(""),
    '974': u(""),
}


STATES = {
    'AP': u("Andhra Pradesh"),
    'AR': u("Arunachal Pradesh"),
    'AS': u(""),
    'BR': u(""),
    'CG': u(""),
    'GA': u(""),
    'GJ': u(""),
    'HR': u(""),
    'HP': u(""),
    'JK': u(""),
    'JH': u(""),
    'KA': u(""),
    'KL': u(""),
    'MP': u(""),
    'MH': u(""),
    'MN': u(""),
    'ML': u(""),
    'MZ': u(""),
    'NL': u(""),
    'OD': u(""),
    'PB': u(""),
    'RJ': u(""),
    'SK': u(""),
    'TN': u(""),
    'TS': u(""),
    'TR': u(""),
    'UP': u(""),
    'UK': u(""),
    'WB': u(""),
    'AN': u(""),
    'CH': u(""),
    'DN': u(""),
    'DD': u(""),
    'LD': u(""),
    'DL': u(""),
    'PY': u(""),
}


with open(os.path.join(
        os.path.dirname(__file__),
        'in.districts.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class Districts(IntCodeMixin, BaseMap):
    """Indian Districts map"""
    x_labels = list(DISTRICTS.keys())
    area_names = DISTRICTS
    area_prefix = 'z'
    kind = 'district'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'in.states.svg')) as file:
    REG_MAP = file.read()


class States(IntCodeMixin, BaseMap):
    """Indian States map"""
    x_labels = list(STATES.keys())
    area_names = STATES
    area_prefix = 'a'
    svg_map = REG_MAP
    kind = 'state'


DISTRICTS_STATES = {
    "01": "82",
    "02": "22",
    "03": "83",
    "04": "93",
    "05": "93",
    "06": "93",
    "07": "82",
    "08": "21",
    "09": "73",
    "10": "21",
    "11": "91",
    "12": "73",
    "13": "93",
    "14": "25",
    "15": "83",
    "16": "54",
    "17": "54",
    "18": "24",
    "19": "74",
    "21": "26",
    "22": "53",
    "23": "74",
    "24": "72",
    "25": "43",
    "26": "82",
    "27": "23",
    "28": "24",
    "29": "53",
    "2A": "94",
    "2B": "94",
    "30": "91",
    "31": "73",
    "32": "73",
    "33": "72",
    "34": "91",
    "35": "53",
    "36": "24",
    "37": "24",
    "38": "82",
    "39": "43",
    "40": "72",
    "41": "24",
    "42": "82",
    "43": "83",
    "44": "52",
    "45": "24",
    "46": "73",
    "47": "72",
    "48": "91",
    "49": "52",
    "50": "25",
    "51": "21",
    "52": "21",
    "53": "52",
    "54": "41",
    "55": "41",
    "56": "53",
    "57": "41",
    "58": "26",
    "59": "31",
    "60": "22",
    "61": "25",
    "62": "31",
    "63": "83",
    "64": "72",
    "65": "73",
    "66": "91",
    "67": "42",
    "68": "42",
    "69": "82",
    "70": "43",
    "71": "26",
    "72": "52",
    "73": "82",
    "74": "82",
    "75": "11",
    "76": "23",
    "77": "11",
    "78": "11",
    "79": "54",
    "80": "22",
    "81": "73",
    "82": "73",
    "83": "93",
    "84": "93",
    "85": "52",
    "86": "54",
    "87": "74",
    "88": "41",
    "89": "26",
    "90": "43",
    "91": "11",
    "92": "11",
    "93": "11",
    "94": "11",
    "95": "11",
    "971": "01",
    "972": "02",
    "973": "03",
    "974": "04",
    "975": "05",
    "976": "06"
}


def aggregate_states(values):
    if isinstance(values, dict):
        values = values.items()
    states = defaultdict(int)
    for district, value in values:
        states[DISTRICTS_STATES[district]] += value
    return list(states.items())
