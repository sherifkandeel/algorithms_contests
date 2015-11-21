import sys
sys.setrecursionlimit(1500)
reachedEnd = False
def navigate(grid, visited, c, r):   
    #print c, r, len(grid), len(grid[0])
    global reachedEnd
    if r>= len(grid):
        reachedEnd = True
        return
    
    if c<0 or c>= len(grid[0]) or r<0:
        return
    
   
    
    if visited[r][c]:
        return
    if grid[r][c] == 'R':
        return
        
    visited[r][c] = True
    navigate(grid, visited, c+1, r)
    navigate(grid, visited, c-1, r)
    navigate(grid, visited, c, r+1)


w, h = map(int, raw_input().split(' '))
grid = []
for i in range(h):
    grid.append(list(raw_input().strip()))
visited = [[False for i in range(w)] for j in range(h)]
yc = grid[0].index('Y')
navigate(grid, visited, yc, 0)
if reachedEnd:
    print "YES"
else:
    print "NO"

