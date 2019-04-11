# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:08:36 2019

@author: Tara
"""
import numpy as np

N = 100
TOL = 10**(-4)
tol = 2
z0 = 2
itter=0
My_array = np.zeros([0,2])

f_z= lambda x: x**3
j_z= lambda x: 3*x**2

while tol > TOL and itter < N:
    z1 = z0 - (f_z(z0)/j_z(z0))
    tol = abs(z1 - z0)
    z0 = z1
    itter += 1
    My_array = np.vstack([My_array,np.array([z1,tol])])
    
print(My_array)
    
#1/100*[x**4+(e-2-np.sqrt(2))*x**3+(2*np.sqrt(2)-np.sqrt(2)*e-3-2*e)*x**2+(2*np.sqrt(2)*e+3*np.sqrt(2)-3*e)*x+3*np.sqrt(2)*e]=0