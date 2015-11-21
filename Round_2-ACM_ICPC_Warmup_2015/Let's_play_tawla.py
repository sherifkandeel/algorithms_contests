d = {}
d[1] = "Yakk"
d[2] = "Doh"
d[3] = "Seh"
d[4] = "Ghar"
d[5] = "Bang"
d[6] = "Sheesh"
d[11] = "Habb Yakk"
d[22] = "Dobara"
d[33] = "Dousa"
d[44] = "Dorgy"
d[55] = "Dabash"
d[65] = "Sheesh Beesh"
d[66] = "Dosh"

t = input()
for i in range(t):
    a, b = map(int, raw_input().split(' '))
    bigger = max(a,b)
    smaller = min(a,b)

    if bigger == smaller:
        print "Case %d: %s"%(i+1, d[bigger*11])
    elif bigger == 6 and smaller == 5:
        print "Case %d: %s"%(i+1, d[65])
    else:
        print "Case %d: %s %s"%(i+1, d[bigger], d[smaller])
    
