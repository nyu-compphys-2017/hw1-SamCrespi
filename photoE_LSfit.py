# -*- coding: cp1252 -*-
# This program fits a sample of
#   photoelectric effect mesurements
#   with least-square method

#----------------------------------------------

# Import packages

import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt

#----------------------------------------------

# Import constants

#from scipy.Constants import e,h <------ doesn't work
e = 1.602e-19
h = 6.626070040e-34

#----------------------------------------------

# Read file

values = loadtxt('millikan.txt',float)
a = []
b = []

for i in range(0,len(values)):
    a += [values[i,0]]
    b += [values[i,1]]

x = np.array(a,float)
y = np.array(b,float)

#----------------------------------------------

# Least-square fit

N = len(values)
E_x = sum(x)/N
E_y = sum(y)/N
E_xx = sum(x*x)/N
E_xy = sum(x*y)/N

m = (E_xy - E_x*E_y)/(E_xx - E_x**2)
c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2)

print 'Best-fit line values: m=',m,'; c=',c

#----------------------------------------------

# Plot

y_teo = x*m + c

plt.plot(x,y,'k.',x,y_teo)
plt.xlabel('frequency [Hz]')
plt.ylabel('voltage [V]')
plt.show()

#----------------------------------------------

# Evaluate h

h_mis = m*e

print 'Measured value for h: ', h_mis
print 'that differs from the accepted value of h by ', (h-h_mis)*100/h, '%'

