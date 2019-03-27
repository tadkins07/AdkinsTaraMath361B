# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:56:52 2019

@author: Tara
"""

import numpy as np

divisors = []
def divide(n):
    for ii in range(1,n):
        if n % ii == 0:
            divisors.append(ii)
            
    print(divisors)
    
divide(500)