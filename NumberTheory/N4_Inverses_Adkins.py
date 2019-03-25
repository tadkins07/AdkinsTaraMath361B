# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:53:04 2019

@author: Tara
"""

import numpy as np
m= 6
inverses=[]

for x in range(1,m):
     for y in range(1,m):
         if (x + y) % m == 1:
            zeros.append([x,y])
            
print('The elements and their inverses are',zeros)