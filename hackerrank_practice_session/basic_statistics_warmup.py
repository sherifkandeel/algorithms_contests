import collections
import math
def mean(m):
    return float(sum(m))/float(len(m))

def median(m):
    m.sort()
    if len(m) % 2 == 0:
        return float(m[len(m)/2]+m[len(m)/2-1])/2.0
    return float(m[len(m)/2])

def mode(m):
    counter = collections.Counter(m)
    ls = counter.most_common()
    largest = ls[0][1]
    sls = []
    for t in ls:
        if t[1] == largest:
            sls.append(t[0])
    sls.sort()
    return sls[0]
        

def sd(m):
    sd = 0
    med = mean(m)
    for i in m:
        sd += (i-med)*(i-med)
    sd /= len(m)
    return float(math.sqrt(sd))


def boundaries(m):
    mn = mean(m)
    s = sd(m)/math.sqrt(len(m))
    lb = mn - (1.96)*s
    up = mn + (1.96)*s 
    return "{0:.1f}".format(lb)+" "+ "{0:.1f}".format(up)


raw_input()
m = map(int, raw_input().split(' '))
print "{0:.1f}".format(mean(m))    
print "{0:.1f}".format(median(m))    
print mode(m)   
print "{0:.1f}".format(sd(m))    
print boundaries(m)
