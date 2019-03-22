# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:16:19 2019

@author: Tara
"""

import numpy as np

primes = []
num = 3

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
    
while True:
    if prime_check(num):
        primes.append(num)
    else:
        for ii in primes:
            x = np.sqrt(((num-ii)/2))
            if x.is_integer()==True:
                break
        else:
            print(num, 'is the first odd composite number the conjecture does not hold true for')
            break
    num += 2
                    