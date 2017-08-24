#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:32:45 2017

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

S0 = np.array(g_data[0])  # Time
S1 = np.array(g_data[1])  # Temperature
S2 = np.array(g_data[2])  # Wind
S3 = np.array(g_data[3])  # Solar
S4 = np.array(g_data[4])  # Humidity
S5 = np.array(g_data[5])  # IsHoliday
S6 = np.array(g_data[6])  # Day of the Week
S7 = np.array(g_data[7])

y = np.array(g_data[8])  # Whole Building Energy
func = (((636.4469 + np.cos(S6)))/(np.log((1069.5890 * ((((((((((np.sin(((-1491.0946) - (S7 - 1541.5198))))/((np.exp(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))) - (-0.1508)))))/(np.exp((np.sin(np.sin(((S3)/(1053.8509)))) - (-0.0004))))))/(np.tanh(np.exp(np.log(S6))))))/(np.exp(np.sin(np.sin(np.tanh(np.sin(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))))))))))/(np.tanh(np.exp((np.tanh((np.log(S3) - np.exp(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))))) - (-0.0004))))))))))

z = (np.vstack((func, y, S5, S6, S7))).T
