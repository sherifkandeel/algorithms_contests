import copy
def generate(ls, cur, num, n, k):
    if num > 0:
        cur.append(num)
    if len(cur) == k:
        ls.append(cur)
        return
    for i in range(num+1, n+1):
        generate(ls, copy.deepcopy(cur), i, n, k)
            
            
def combine(n, k):
    ls = []
    generate(ls, [], 0, n, k)
    return ls

def get_xor(lst):
    res = 0
    for i in lst:
        res ^= i
    return res

def get_sets(lst):
    lss = []
    for s in lst:
        lss.append(set(s))
    return lss

def common_elements(i, j, sets):
    for e in i:
        if e in sets(j):
            return False
    return True

n, m = map(int, raw_input().split(' '))
ls = []
for i in range(1, n+1):
    ls.extend(combine(n,i))

xors = []
for s in ls:
    xors.append(get_xor(s))
   
sets = []
sets = get_sets(ls) 

count = 0
for i in range(len(ls)):
    for j in range(len(ls)):
        if i == j:
            continue
        if xors(ls[i]) < xors(ls[j]) and common_elements(i,j,sets) == False:
            count +=1

print count%m



