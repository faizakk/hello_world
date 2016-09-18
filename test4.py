#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
d1=0
d2=0
for i in range(0,n):
    d1=d1+a[i][i]
print d1    

for i in range(0,n):
    d2=d2+a[i][n-i-1]
print d2    

print abs(d1-d2)

