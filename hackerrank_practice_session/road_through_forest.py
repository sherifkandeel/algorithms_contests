#this works but takes long time
import copy
def get_minimum_trees(forest):
    for i in range(len(forest[0])):
        # visited = [[False for x in range(len(forest[0]))] for y in range(len(forest))]
        visited = set()
        navigate(0,i,forest, visited,0)

_max_count = 20
smallest_ones_count = _max_count
def navigate(row, col, forest, visited, onesCount):
    global smallest_ones_count
    if row < 0 or col< 0 or row>=len(forest) or col>=len(forest[0]):
        return
    # if visited[row][col]:
    if (row,col) in visited:
        return


    if forest[row][col] == 1:
        onesCount+=1
    # visited[row][col] = True
    visited.add((row,col))
    
    if onesCount > smallest_ones_count:
        return
    #we arrived
    if row == len(forest) -1:
        if smallest_ones_count > onesCount:
            smallest_ones_count = onesCount
        return
    
    new_visited = set()
    for i in visited:
        new_visited.add(i)

            
    navigate(row+1, col-1, forest, new_visited , onesCount)
    navigate(row+1, col,   forest, new_visited, onesCount)
    navigate(row+1, col+1, forest, new_visited, onesCount)
    navigate(row, col+1,   forest, new_visited, onesCount)
    navigate(row, col-1,   forest, new_visited, onesCount)
    navigate(row-1, col,   forest, new_visited, onesCount)
    navigate(row-1, col-1, forest, new_visited, onesCount)
    navigate(row-1, col+1, forest, new_visited, onesCount)

    return







t = input()
for i in range(t):
    smallest_ones_count = 450
    smallest_path = []
    n, m = map(int, raw_input().strip().split(' '))
    _max_count = n
    forest = [[0 for x in range(m)] for y in range(n)]
    for j in range(n):
        forest[j] = map(int, raw_input().strip().split(' '))
    get_minimum_trees(forest)
    print smallest_ones_count



