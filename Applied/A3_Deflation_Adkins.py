# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:48:09 2019

@author: Tara
"""

def r_empty():
    empty = True
    for i in r:
        if i != 0:
            empty = False
            break
    return empty   
            
def r_divides_g():
    if len(r) >= len(g):
        return True
    else:
        return False
    
def divisionAddQ(x,y): #r[-1] g[-1]
    if len(r)==len(g):
        q.append(r[-1]/g[-1])
    else:
        for i in range(0, len(r)-len(g) - 1):
            q.insert(i,0)
        q.insert(len(r)-len(g),r[-1]/g[-1])
    return q
        
def multiplying_g_and_sub():
    for i in range(0,len(g)):
        g[i] = (g[i]*q[-1])*-1
    for i in range(0,len(q) - 1):
        g.insert(0,0)
    for i in range(0,len(g)):
        print("at",i,"r equals ", r[i] , "+", g[i])
        r[i]=r[i]+g[i]
    return r

f = [-1,0,0,1]
g = [2,1]
r = list(f)
q = [0]

while (r_empty == False) and (r_divides_g) == True:
    q = divisionAddQ(r[-1], g[-1])
    r = multiplying_g_and_sub()
"""
q = divisionAddQ(r[-1], g[-1])
r = multiplying_g_and_sub()
"""
print(q)
print(r)