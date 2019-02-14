# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:45:14 2019

@author: Tara
"""

N = 1000

import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,N)
def f(x):
    if x.any() <-2:
        return -3*(x+2)**2+1
    elif -2<= x.any() and x.any() < -1:
        return 1
    elif -1 <= x.any() and x.any() <= 1:
        return (x-1)**3 +3
    elif 1< x.any() and x.any() < 2:
        return np.sin(math.pi*x) +3
    else:
        3*math.sqrt(x-2)+4
        
y= f(x) 

plt.plot(x,y)

plt.xlabel('x axis')

plt.ylabel('y axis')
plt.title('Piecewise Plot')

plt.show
