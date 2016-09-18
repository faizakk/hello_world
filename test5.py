#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

a=0
b=0
c=0
for i in range(0,n):
    if arr[i]<0:
        a=a+1
    if arr[i]==0:
        b=b+1
    if arr[i]>0:
        c=c+1
d=(a+b+c)


print float(c)/float(d)
print float(a)/float(d)
print float(b)/float(d)        
        