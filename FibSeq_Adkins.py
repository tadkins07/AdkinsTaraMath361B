# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:24:27 2019

@author: Tara
"""

N = 100

F0 = 0
F1 = 1
F2= 1

F=[F0,F1]
for nn in range(N):
    F.append(F[nn]+F[nn+1])
    

C= [F1,F2]
for nn in range(N):
    C.append(F[nn]**2 - F[nn+1]*F[nn-1])
    
print('last 10 terms of the sequence are', C[-10:])

