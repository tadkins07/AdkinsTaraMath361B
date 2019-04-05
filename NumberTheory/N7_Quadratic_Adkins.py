# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:05:04 2019

@author: Tara
"""

import numpy as np

def prime_check(x): 
    if x > 1:
        for ii in range(2,x):
            if x % ii == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
p = 12
count = np.array([0,2])
neg_one = np.array([0,'true'])
 
for ii in range(2,p+1):
    if prime_check(i) == True:
        residues = []
        count = 0
        for jj in range(0,i):
            value=(jj * jj)%i
            if residues.count(value)==0:
                count += 1
                residues.append(value)
            if residues.count(i-1)>0:
                neg_one = np.vstack ([neg_one, np.array([i,"true"])])
            else: 
                neg_one = np.vstack([neg_one, np.array([i,"false"])])
                
            count = np.vstack([count, np.array(i,count)])
    
print('The number of residues of z mod p is :\n', count[1:][:])
print('The chart for if -1 is a residue of z mod p is :\n', neg_one[1:][:])
        