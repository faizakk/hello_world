#!/usr/bin/py
def lonelyinteger(a):
    c=0
    for i in range(0,len(a)):
        c= c ^ a[i]
    answer=c
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

