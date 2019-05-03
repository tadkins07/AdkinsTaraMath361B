# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:36:53 2019

@author: Tara
"""

n = 50

def Function(m, n):
    differentways = [1] * m + [0] * (n-m+1)
    for j in range(m, n+1):
        differentways[j] += differentways[j - 1] + differentways[j - m]
    return differentways[n] - 1

red = Function(2,n)
green = Function(3,n)
blue = Function(4,n)

print ("Space size =", n, "units")
print (red)
print (green)
print(blue)
print ("Number of ways to fill:", red+green+blue)