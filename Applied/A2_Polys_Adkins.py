# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:49:08 2019

@author: Tara
"""

p = [-4, 6, 2, 0]
#my polynomial is 2x^2 + 6x - 4 
j = []
h = []

def polynomial(x):
    for ii in range(len(p)):
        k = x**i
        j.append(p[ii]*l)
        return sum(j)
    print(sum(p(-4)))
    
def p_derivative(n):
    for ii in range(len(p)):
        n = p[ii]*ii
        h.append(n)
        return h
    for l in range(len(h)):
        f = x**i
        h.append(m[l]*f)
    return h[1:]
        
print(p_derivative(-4))