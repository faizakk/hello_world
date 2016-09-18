import sys
import re

time = raw_input().strip()
#.split()

l=len(time)
t1=time.rsplit(':')
hour =  t1[0]
minute= t1[1]
second=t1[2][0:2]
t=t1[2][2:4]

if (int(hour) >12)|(int(hour)<0):
    print "Error! Hour should be between 0 and 12"
    sys.exit()

if (int(minute) >59)|(int(minute)<0):
    print "Error! Minute should be between 0 and 59"
    sys.exit()

if (int(second) >59)|(int(second)<0):
    print "Error! Second should be between 0 and 59"
    sys.exit()

print hour
print minute
print second
print t
if (t=='PM') and (int(hour)!=12):
    h=int(hour)+12
    print str(h)+':'+minute+':'+second
elif (t=='AM') and (int(hour)==12):
    h='00'
    print h+':'+minute+':'+second   
else:
    print hour+':'+minute+':'+second


#second=t1[2].split('P')[0]
#t=t1[2].split('P')

#sec=second.split('A')[0]
#print re.split(r'[:]|[a-z]*', time)
#second= time.rsplit('A', l)[2]
#t=      time.rsplit(' ', 3)[3]
#print time.rsplit(':', 1)[1]
#for j in (0,l)