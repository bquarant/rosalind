#!/usr/bin/env python
'''
Problem Title: Strings and Lists
Rosalind Python ID: INI3
Rosalind Python #: 003
URL: http://rosalind.info/problems/ini3/
'''

'''
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
'''

s = 'FZoaYpVzH4NzKWpTMisvcEDHOhxbuXwdldKUsIomachus4rs5e6KK4Jj2Fw0M6rJNDJKZfIx7HDEoN1CR2TveXd4CWYnPc0VtmBQUhdQQRsv9Z8SAPi9pXvnc4BwWqogUZCidRvodK8zeKdqZBVJ8JhyXeruXkrwXLk2iBK8s3wumuzusumeiL4gLKeMUCWKhl.'
a = 37
b = 44
c = 170
d = 179
output = s[a:b+1] + " " + s[c:d+1]
print output
