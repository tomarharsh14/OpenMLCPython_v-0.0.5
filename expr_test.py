# -*- coding: utf-8 -*-
# MLC (Machine Learning Control): A genetic algorithm library to solve chaotic problems
# Copyright (C) 2015-2017, Thomas Duriez (thomas.duriez@gmail.com)
# Copyright (C) 2015, Adrian Durán (adrianmdu@gmail.com)
# Copyright (C) 2015-2017, Ezequiel Torres Feyuk (ezequiel.torresfeyuk@gmail.com)
# Copyright (C) 2016-2017, Marco Germano Zbrun (marco.germano@intraway.com)
# Copyright (C) 2016-2017, Raúl Lopez Skuba (raulopez0@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
sys.path.append("/home/htomar/MLC-0.0.5/MLC-0.0.5")
import binascii
import numpy as np
import struct
import MLC.Log.log as lg

from MLC.Common.LispTreeExpr.LispTreeExpr import LispTreeExpr
from MLC.Log.log import set_logger
from MLC.mlc_parameters.mlc_parameters import Config


def initialize_config():
    config = Config.get_instance()
    config.read('/home/htomar/MLC-0.0.5/Clone_18/Clone_18.conf')
    return config

# Set printable resolution (don't alter numpy interval resolution)
np.set_printoptions(precision=9)
# Show full arrays, no matter what size do they have
np.set_printoptions(threshold=np.inf)
# Don't show scientific notation
np.set_printoptions(suppress=True)

initialize_config()
set_logger('console')

# Full expression
expr6 = "(root (/ (+ 636.4469 (cos S6)) (log (* 1069.5890 (/ (/ (/ (/ (/ (sin (- -1491.0946 (- S7 1541.5198))) (- (exp (sin (- -701.6797 (- 394.8346 (- S5 0.5484))))) -0.1508)) (exp (- (sin (sin (/ S3 1053.8509))) -0.0004))) (tanh (exp (log S6)))) (exp (sin (sin (tanh (sin (sin (- -701.6797 (- 394.8346 (- S5 0.5484)))))))))) (tanh (exp (- (tanh (- (log S3) (exp (sin (- -701.6797 (- 394.8346 (- S5 0.5484))))))) -0.0004))))))))"
expr61 = "(root (exp (- -6.3726 (* -7.1746 S0))))"
expr612 = "(root (- -6.3726 (* -7.1746 S0)))"

tree = LispTreeExpr(expr6)
out = LispTreeExpr.formal(tree)
print out