import sys
def getfirstless(original, arr, threshold, a, b):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start)/2
        if arr[mid] < threshold and isvalidtriangle(original, a, b, mid):
            start = mid + 1
        # if arr[mid] >= threshold:
        # elif arr[mid] < threshold:
        else:
            end = mid - 1
    return end 

def getfirstmore(original, arr, threshold, a , b):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start)/2
        if arr[mid] > threshold and isvalidtriangle(original, a, b, mid):
            end = mid - 1
        # elif arr[mid] <= threshold:
        else:
            start = mid + 1
    return end + 1 

def isvalidtriangle(arr, a, b, c):
    a = arr[a]
    b = arr[b] 
    c = arr[c]
    return a+b> c and a+c > b and b+c > a

# N = int(raw_input().strip())
# A = map(int,raw_input().strip().split(' '))
N = 6
A = [2, 3, 9, 10, 12, 15]
squares = []
for i in A:
    squares.append(i*i)

acute = 0
obtuse = 0
right = 0
sdict = {squares[i]:i for i in range(len(A))}
for i in range(N):
    for j in range(i, N):
        if i==j: continue
        langle = squares[i] + squares[j]
        if langle in sdict:
            right +=1
            # obtuse += N-sdict[langle]
            # acute += sdict[langle]
            # continue
        
        idx = getfirstmore(A, squares, langle, i, j)
        if idx != len(A):
            obtuse += (N-idx)
        less = getfirstless(A, squares, langle, i, j)
        print A[i], A[j], A[less]
        if less != -1:
            acute += less

print acute, right, obtuse
        
        
        

        
    



# print A[getfirstless(A, 10)]
# print A[getfirstmore(A, 15)]


    
    
# your code goes here

