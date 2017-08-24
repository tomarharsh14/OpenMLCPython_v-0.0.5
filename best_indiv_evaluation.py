"""
Created on Thu Aug 24 11:32:45 2017
@author: htomar
"""

import sys
sys.path.append("/home/htomar/MLC-0.0.5/MLC-0.0.5")

import numpy as np
import csv

from MLC.Common.LispTreeExpr.LispTreeExpr import LispTreeExpr
from MLC.Log.log import set_logger
from MLC.mlc_parameters.mlc_parameters import Config

def initialize_config():
    config = Config.get_instance()
    config.read('/home/htomar/MLC-0.0.5/Clone_20/Clone_20.conf')
    return config


# Set printable resolution (don't alter numpy interval resolution)
np.set_printoptions(precision=9)
# Show full arrays, no matter what size do they have
np.set_printoptions(threshold=np.inf)
# Don't show scientific notation
np.set_printoptions(suppress=True)


g_data = None
with open('/home/htomar/Energy_Testing.csv', 'r') as f:
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

# func = (((636.4469 + np.cos(S6)))/(np.log((1069.5890 * ((((((((((np.sin(((-1491.0946) - (S7 - 1541.5198))))/((np.exp(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))) - (-0.1508)))))/(np.exp((np.sin(np.sin(((S3)/(1053.8509)))) - (-0.0004))))))/(np.tanh(np.exp(np.log(S6))))))/(np.exp(np.sin(np.sin(np.tanh(np.sin(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))))))))))/(np.tanh(np.exp((np.tanh((np.log(S3) - np.exp(np.sin(((-701.6797) - (394.8346 - (S5 - 0.5484))))))) - (-0.0004))))))))))

func = "(root (/ (+ 636.4469 (cos S6)) (log (* 1069.5890 (/ (/ (/ (/ (/ (sin (- -1491.0946 (- S7 1541.5198))) (- (exp (sin (- -701.6797 (- 394.8346 (- S5 0.5484))))) -0.1508)) (exp (sin (sin (tanh (sin (tanh (/ S3 1053.8509)))))))) (tanh (exp (/ (tanh (/ (/ S3 1053.8509) 0.1508)) 0.1508)))) (exp (sin (sin (/ (sin (tanh (sin (tanh (/ S3 1053.8509))))) (- (/ S3 1053.8509) -0.1508)))))) (tanh (exp (/ (/ (/ (/ S3 1053.8509) (- (- (sin (tanh (/ S3 1053.8509))) -0.0004) -0.1508)) (- (cos (/ -1994.7186 S5)) -0.1508)) (tanh (exp (sin S6)))))))))))"

initialize_config()
# Don't log anything
set_logger('testing')

# Evaluate the expression
tree = LispTreeExpr(func)
b = tree.calculate_expression([S0, S1, S2, S3, S4, S5, S6, S7]) 

# Compare the expressions
#==============================================================================
# z = (np.vstack((b, y, S5, S6, S7))).T
# for index in xrange(len(z)):
#     print ("Index: {}\t func: {}\t y: {}\t S3: {}\t S5: {}\t S6: {}\t S7: {}"
#            .format(index, z[index][0], z[index][1], S3[index], S5[index], S6[index], S7[index])) 
#==============================================================================

y_mean = np.mean(y)
sq_diff = np.dot((y-b), (y-b))
CV = np.sqrt(sq_diff/len(b))/y_mean
print CV
