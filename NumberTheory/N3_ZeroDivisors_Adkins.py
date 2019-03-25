# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:03:39 2019

@author: Tara
"""

import numpy as np

m=10
zeros=[] 

for x in range(1,m):
     for y in range(1,m):
         if (x * y) % m == 0:
            zeros.append([x,y])
            
print('Zero divisors are',zeros)
