# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:43:56 2019

@author: Tara
"""

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
    
primes = 20
primelist = []
check = 2

while len(primelist) < primes:
    prime = False
    while prime == False:
        prime = prime_check(check)
        check += 1
        
    primelist.append(check-1)
    
print('List of the first {} primes: {}'.format(primes,primelist))

