# -*- coding: cp1252 -*-
# This program plots a Mandelbrot set with N iterations

#----------------------------------------------

# Import packages and time

import numpy as np
import matplotlib.pyplot as plt

import time
start_time = time.time()

#----------------------------------------------

# Define plot features

points=10000000
iters=100

x_min = -2.
x_max = 2.
y_min = -2.
y_max = 2.

#----------------------------------------------

# Generate random complex distribution

x = np.random.rand(points)*(x_max-x_min) + x_min
y = np.random.rand(points)*(y_max-y_min) + y_min

z = []

for (a, b) in zip(x, y) :
    zz = complex(a, b)
    z += [zz]

z = np.array(z,complex)

#----------------------------------------------

# Distinguish point of Mandelbrot set

control=np.zeros(points,int)

for i in range(0, points):
    c = z[i]
    old_z=0
    for ii in range(0, iters):
        new_z=(old_z**2) + c
        if np.absolute(new_z) > 2:
            control[i]=1
            break
        old_z=new_z
    prog=(i*100.)/points
    if prog==(i*100.)//points:
        print 'Progress: ', int(prog),'%'

z_M = []
#z_notM = [] #>>>>>>>> useless, I need memory

for i in range(0, points):
    if control[i]==0: z_M += [z[i]]
    #else: z_notM += [z[i]]

z_M = np.array(z_M,complex)
#z_notM = np.array(z_notM,complex)

print 'Percentage of Mandelbrot points: ', len(z_M)*100/points,'%'

#----------------------------------------------

# Plot of Mendelbrot set
s=0.9
plt.plot(z_M.real,z_M.imag,'k.',ms=s)

time = time.time() - start_time
print 'Time: ', time//60, 'min ', time%60, 's'

plt.show()



