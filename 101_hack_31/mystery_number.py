# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
a = map(int, raw_input().split(' '))
b = map(int, raw_input().split(' '))
a.sort()
b.sort()
done = False
for i in range(len(a)):
    if a[i] != b[i]:
        print b[i]  
        done = True
        break
        
if not done:
    print b[-1]

