# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:02:40 2019

@author: Tara
"""

import numpy as np

N = 100

List1=[]
product1 = 1
for i in range(2,N):
    temp=(i**3-1)/(i**3+1)
    product1*=temp
    List1.append(product1)
    
print('First 15 Terms of p_n Sequence',List1[:15])
print('Last 15 Terms of p_n Sequence',List1[-15:])

List2=[]
product1 = 1
for i in range(1,N):
    temp=(np.exp(i/100)/i**10)
    product1*=temp
    List2.append(product1)
    
print('First 15 Terms of q_n Sequence', List2[:15])
print('Last 15 Terms of q_n Sequence', List2[-15:])

List3=[]
product1= 1
for i in range(1,N):
    temp=(np.exp(i/2)/np.sqrt(i))
    product1*=temp
    List3.append(product1)
    
print('First 15 Terms of m_n Sequence', List3[:15])
print('Last 15 Terms of m_n Sequence', List3[-15:])
        

