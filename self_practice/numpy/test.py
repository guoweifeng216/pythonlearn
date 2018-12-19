#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/19 11:54
@filename:test

"""
import numpy as np
vector = np.ones([8,9], int)
print(np.ones([8,9], int))
print(np.pad(vector,pad_width=1,mode='constant',constant_values=0))
# print(np.array(0) // np.array(0))
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
print(np.random.uniform(-10,+5,5))
print(np.random.randint(0,10,10))
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(Z1,Z2)
print(np.intersect1d(Z1,Z2))
# print(np.sqrt(-1))
print(np.emath.sqrt(-1))
# print(np.sqrt(-1) == np.emath.sqrt(-1))
print(np.ones(3)*2)
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
print(np.add(A,B,out=B))
print(np.divide(A,2,out=A))
print(np.negative(A,out=A))
print(np.multiply(A,B,out=A))