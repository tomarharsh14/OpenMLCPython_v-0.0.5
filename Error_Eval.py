#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:14:08 2017

@author: htomar
"""

import numpy as np
import csv

global g_data

g_data = None
with open('/home/htomar/Energy_Training.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        if g_data is None:
            g_data = [[] for x in xrange(len(row))]

        for index in xrange(len(row)):
            g_data[index].append(float(row[index]))


y = np.array(g_data[8])  # Whole Building Energy

 # Data from OpenMLC directly
b = np.loadtxt('/home/htomar/MLC-0.0.5/test.out')

y_mean = np.mean(y)
sq_diff = np.dot((y-b), (y-b))
CV = np.sqrt(sq_diff/len(b))/y_mean


