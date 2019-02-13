# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:10:43 2019

@author: Tara
"""

N = 10000

F0 = 0
F1 = 1
m= 2

F=[F0,F1]
multiples=[]
for nn in range(N):
    F.append(F[nn]+F[nn+1])
    
for nn in F:
    if nn % m == 0:
        multiples.append(nn)
    
print(multiples)
print(F)