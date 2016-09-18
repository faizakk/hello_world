
def ins_sort():
    n= int(raw_input())
    a=[0]*n
    for i in range (0,n):
        #a[i]=raw_input().strip().split()
        a[i]= int(raw_input())
      
   # a = [int(i) for i in raw_input().strip().split()]
    num=0
    print a

    for j in range(1,n):
        b=a[j]
        i=j-1
        while i>=0:
            if b<a[i]:
                a[i+1]=a[i]
                a[i] =b
                i=i-1
                num=num+1
            else:
                break
    print 'hello',a
    print 'number',num
    
    
ins_sort()