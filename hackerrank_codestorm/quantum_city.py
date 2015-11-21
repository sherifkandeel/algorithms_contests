import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    guards = 0
    for i in range(n):
        if i == 0:
            continue
        if a[i] == 0 and a[i-1] == 0:
            a[i] = 1
            guards +=1 
    print guards
            
