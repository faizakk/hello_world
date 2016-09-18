# Enter your code here. Read input from STDIN. Print output to STDOUT
print 'Enter the n,m,q:'
c=raw_input().strip().rsplit(' ')
n=int(c[0])
m= int(c[1])
q=int(c[2])
a=[0]*n
b=[0]*n
ans=[0]*q
print 'Enter the array:'
a=raw_input().strip().rsplit(' ')
print a
#for i in range(0,n):
   # a[i]=int(raw_input())
w=a[0]    
for i in range(0,n):
    b[((i+m)%n)]=a[i]
   
print b
    
for i in range(0,q):
    i=int(raw_input())
    print b[i]