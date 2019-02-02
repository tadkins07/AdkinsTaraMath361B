# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:39:22 2019

@author: Tara
"""

x=2
y=3
z=4

mylist=[]
Component1=x+y
Component2=y*z+3*x
Component3=Component1**2 +3
Component4=(2*(Component2)-(.5*x)/(Component1))
Component5=7%3

Component3 += 3
Component5*3/4

mylist=[Component1,Component2,Component3,Component4,Component5]

print(sum(mylist))
