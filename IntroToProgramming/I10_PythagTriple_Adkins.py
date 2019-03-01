# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:00:31 2019

@author: Tara
"""

import numpy as np

triples = np.zeros([0,4])

for a in range(1,500):
    for b in range(a,500):
        for c in range (b, 500):
            if a**2+b**2 == c**2:
                triples = np.vstack( [triples, np.array([a,b,c,a+b+c])])
    
print(triples[np.where(triples[:,3]==1026)], 'is the pythagorean triple that sums to 1026.')

