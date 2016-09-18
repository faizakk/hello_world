#!/bin/python

import sys

n = int(raw_input().strip())

temp=n
for j in range (1,n+1):
    t= ' '
    s ='#'
    print t*(temp-1)+s*(n-temp+1)
    temp=temp-1    
    
       
print '\n'        


