from collections import deque
class Solution(object):
    def closedIsland(self, grid):
        answer = 0
        q = deque()
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs() : 
            while q:
                x,y = q.popleft()
                if 0<=x<len(grid) and 0<=y<len(grid[0]):
                    if grid[x][y]==0:
                        grid[x][y]=1
                        for i in range(4):
                            dx=x+direction[i][0]
                            dy=y+direction[i][1]
                            q.append((dx,dy))
                 
        for i in range(len(grid)):
            if i==0 or i==len(grid)-1:
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        q.append((i,j))
                        dfs()
            else:
                if grid[i][0]==0:
                    q.append((i,0))
                    dfs()
                if grid[i][len(grid[0])-1]==0:
                    q.append((i,len(grid[0])-1))
                    dfs()
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                if grid[i][j] == 0:
                    answer +=1
                    q.append((i,j))
                    dfs()
        return answer