#!/usr/bin/env python
'''
Problem Title: Variables and Some Arithmetic
Rosalind Python ID: INI2
Rosalind Python #: 002
URL: http://rosalind.info/problems/ini2/
'''

with open('rosalind_ini2.txt') as input_data:
	a, b = map(int, input_data.read().strip().split())

c = a**2 + b**2

print c
with open('INI2.txt', "w") as output_data:
	output_data.write(str(c))
