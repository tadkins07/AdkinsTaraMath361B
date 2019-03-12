# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:11:27 2019

@author: Tara
"""

import numpy as np

N = 200
a0 = 1001

my_list = [a0]
itter = 1
for ii in range(N):
    if a0 % 2 == 0:
        a0 = a0 / 2
    else: 
        a0 = (3*a0)+1
    my_list.append(a0)
    
    if a0 == 1:
        itter += 1
        break
    else:
        itter +=1

print(my_list)
print('it took',itter, 'terms')

