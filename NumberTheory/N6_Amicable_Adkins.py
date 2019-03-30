# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:10:56 2019

@author: Tara
"""

def divide(n):
    divisors = []
    for ii in range(1,n):
        if n % ii == 0:
            divisors.append(ii)
            
    return divisors

N = 10000
amicable_pairs = []
for ii in range(N):
    x = sum(divide(ii))
    if sum(divide(x))== ii and ii != x:
        amicable_pairs.append
    
print('The numbers up to', N ,'are', amicable_pairs)