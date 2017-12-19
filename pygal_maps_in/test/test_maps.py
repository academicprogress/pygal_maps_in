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

from pygal_maps_in.maps import (
    States, Districts,
    STATES, DISTRICTS, aggregate_states)

datas = {}
for dist in DISTRICTS.keys():
    datas[dist] = int(''.join([x for x in dist if x.isdigit()])) * 10


def test_districts():
    fmap = Districts()
    fmap.add('districts', datas)
    q = fmap.render_pyquery()
    assert len(
        q('#districts .district,#dom-com .district')
    ) == len(DISTRICTS)


def test_states():
    fmap = States()
    fmap.add('states', aggregate_states(datas))
    q = fmap.render_pyquery()
    assert len(q('#states .state,#dom-com .state')) == len(STATES)

    assert aggregate_states(datas.items()) == aggregate_states(datas)
