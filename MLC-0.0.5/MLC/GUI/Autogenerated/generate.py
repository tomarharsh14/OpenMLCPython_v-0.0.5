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

import os
import re
import sys
import subprocess

mlc_pyuic5_path = '/opt/mlc-python-2.7.11/bin/mlc_pyuic5'
qtcreator_dir = './mlc_qtcreator'
autogenerate_file = "./autogenerated.py"

# Get all the .ui from the QtCreator project
files = os.listdir(qtcreator_dir)
r = re.compile(r'^.*\.ui$')
files_to_autogenerate = [file for file in files if r.search(file)]

if not files_to_autogenerate:
    print "There are no files to be processed. Aborting program"
    sys.exit(0)

with open(autogenerate_file, "w") as f:
    for file in files_to_autogenerate:
        command = mlc_pyuic5_path + " " + qtcreator_dir + "/" + file
        ret = subprocess.call(command, shell=True, stdout=f)

# Comment the connectSlotsByName line in all files
data = ""
with open(autogenerate_file, "r") as f:
    data = f.read()

data = data.replace("QtCore.QMetaObject.connectSlotsByName", "# QtCore.QMetaObject.connectSlotsByName")
with open(autogenerate_file, "w") as f:
    f.write(data)
