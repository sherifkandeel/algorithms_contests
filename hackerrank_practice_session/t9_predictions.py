#this works correctly, but takes complcated time
#and doesn't support lexiographical order in case two words has the same freq.
import collections
import re
lm = {}
t9 = {}

def build_t9():
    t9['1'] = []
    t9['2'] = ['a','b','c']
    t9['3'] = ['d','e','f']
    t9['4'] = ['g','h','i']
    t9['5'] = ['j','k','l']
    t9['6'] = ['m','n','o']
    t9['7'] = ['p','q','r','s']
    t9['8'] = ['t','u','v']
    t9['9'] = ['w','x','y','z']

def build_lm():
    with open("/home/sherif/personalWork/algorithm_contests/algorithms_contests/hackerrank_practice_session/t9dictionary","r") as f:
        for line in f:
            if not line.isdigit():
                lm[line.replace('\n','')] = 0
    with open("/home/sherif/personalWork/algorithm_contests/algorithms_contests/hackerrank_practice_session/t9TextCorpus", "r") as f:
        for line in f:
            ls = re.findall("([a-zA-Z][[a-zA-Z\-\,]*[a-zA-Z]]*)",line)
            for w in ls:
                if w in lm:
                    lm[w]+=1
                    

def build_possibilities(ns):
    possibilities = []
    for c in ns:
        new_possibilities = []
        for i in t9[c]:
            if len(possibilities) == 0:
                new_possibilities = t9[c]
                break
            new_possibilities.extend([word+i for word in possibilities])
        possibilities = new_possibilities
    possibilities.sort()
    return possibilities

def get_words(plist):
    words = {} 
    for p in plist:
        for w,f in lm.items():
            if w.startswith(p):
                words[w] = f
    slist = sorted(words, key = lambda key: words[key], reverse = True)
    if len(slist) >= 5:
        sslist = slist[0:5]
        return ';'.join(map(str,sslist))
    elif len(slist) > 0:
        slist.sort()
        return ';'.join(map(str,slist))
    else:
        return "No Suggestions"
    


build_lm()
build_t9()
t = int(raw_input())
for i in range(t):
    print get_words(build_possibilities(raw_input()))





        
        


