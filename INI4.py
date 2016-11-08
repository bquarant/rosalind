#!/usr/bin/env python
'''
Problem Title: Conditions and Loops
Rosalind Python ID: INI4
Rosalind Python #: 004
URL: http://rosalind.info/problems/ini4/
'''

'''
Given: Two positive integers a and b (a < b < 10000).
Return: The sum of all odd integers from aa through bb, inclusively.
'''

a = 100
b = 200
s = 0
for i in range(a,b):
    if i % 2 == 1:
        s += i
print s
