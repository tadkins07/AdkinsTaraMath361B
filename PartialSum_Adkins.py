# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:46:16 2019

@author: Tara
"""

import numpy as np

N = 19000

List1=[]
sum1 = 0
for i in range(1,N):
    temp=(np.log((i**4)+i+3))/((np.sqrt(i))+3)
    #print(temp)
    sum1+=temp
    List1.append(sum1)
    #print(sum1)
    
print('First 15 Terms of S_n Sequence',List1[:15])
print('Last 15 Terms of S_n Sequence',List1[-15:])

List2=[]
Sum1 = 0
for i in range(1,N):
    temp=(np.exp(i/100)/i**10)
    Sum1+=temp
    List2.append(Sum1)
    #print(Sum1)
    
print('First 15 Terms of T_n Sequence', List2[:15])
print('Last 15 Terms of T_n Sequence', List2[-15:])

List3=[]
Sum1= 0
for i in range(1,N):
    temp=(np.log(i**2)/np.sqrt(i+1))
    Sum1+=temp
    List3.append(Sum1)
    
print('First 15 Terms of R_n Sequence', List3[:15])
print('Last 15 Terms of R_n Sequence', List3[-15:])
        
