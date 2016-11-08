#!/usr/bin/env python
'''
Problem Title: Working with Files
Rosalind Python ID: INI5
Rosalind Python #: 005
URL: http://rosalind.info/problems/ini5/
'''

'''
f = open('input.txt', 'r') - open file input.txt in read mode
f.read(n) - returns n bytes
f.readlines()[2] - return the third line from the file

- read lines by looping over the file object:
>> for line in f:
>>  print line

- splits
line.split()
.split(",")
.splitlines()

f = open('output.txt', 'w') - open file in write mode...
f.write('Any data you want to write into file')
f.close() - make sure to close any file that you've opened...
'''

'''
Given: Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

def oddlines(filename):
    inp = open(filename, 'r')

    #parse input data into a string
    s = inp.readlines()

    #create array for even line selection loop
    halflines = []

    #select only even lines
    for line in range(len(s)):
        if line % 2 != 0:
            halflines.append(s[line])

    #create output string
    output = ""

    #loop to add each item in array to output string
    for item in halflines:
        output += item

    #test print output
    print output

    #create, write and close output file
    out = open('output.txt', 'w')
    out.write(output)
    out.close()

oddlines("input.txt")
