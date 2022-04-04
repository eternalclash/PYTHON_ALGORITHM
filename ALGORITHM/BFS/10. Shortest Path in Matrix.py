from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        direction =[(1,1),(-1,1),(-1,-1),(1,-1),(1,0),(0,1),(0,-1),(-1,0)]
        q=deque()
        answer=0
        if grid[-1][-1]==1:grid[-1][-1]=99999
        if grid[0][0]==1: return -1
        if len(grid[0])==1 and grid[0][0]==0:return 1
    
        q.append((0,0))
        def bfs():
            while q:
                x,y=q.popleft()
                for i in range(8):
                    dx = x + direction[i][0]
                    dy=  y + direction[i][1]
                    if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy]==0:
                        q.append((dx,dy))
                        if i==0 :
                            grid[dx][dy]=grid[x][y]+1
                        else :
                            grid[dx][dy]=grid[x][y]+1
      
        bfs()
        if grid[-1][-1] == 0 or grid[-1][-1]==99999:
            return -1
        else :
            return grid[-1][-1]+1