# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:21:34 2019

@author: Tara
"""

import numpy as np

N = 10

List1=[]
product1 = 1
a_n= lambda n: 1 + ((n)/(n**3+1))

for i in range(1,N):
    temp=a_n(i)
    product1*=temp
    List1.append(product1)

print('Last 15 Terms of a_n Sequence',List1[-15:])

List2=[]
product1 = 1
b_n= lambda n: 1 + .5**n

for i in range(1,N):
    temp=b_n(i)
    product1*=temp
    List2.append(product1)
 
print('Last 15 Terms of b_n Sequence', List2[-15:])

