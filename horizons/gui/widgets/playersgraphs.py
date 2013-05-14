# Copyright (C) 2008-2013 The Unknown Horizons Team
# team@unknown-horizons.org
# This file is part of Unknown Horizons.
#
# Unknown Horizons is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

import math
from math import sin, cos

import horizons.globals
from fife import fife

from horizons.extscheduler import ExtScheduler
from horizons.util.python.decorators import bind_all
from horizons.util.shapes import Circle, Point, Rect
from horizons.component.namedcomponent import NamedComponent
from horizons.messaging import SettingChanged


class PlayersGraphs(object):
	def __init__(self, session, view, targetrenderer, imagemanager, renderer=None):
		self.session = session
		self.targetrenderer = targetrenderer
		self.imagemanager = imagemanager
		self.renderer = renderer

	def hide(self):
		pass

	def show(self):
		dummy_point0 = fife.Point(0, 0)
		dummy_point1 = fife.Point(0, 0)
		dummy_point0.set(0, 100)
		self.targetrenderer.addLine("a_Name", point0, point1, 50, 50, 50)
