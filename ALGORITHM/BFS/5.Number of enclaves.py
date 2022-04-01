from collections import deque
class Solution(object):
    
    def numEnclaves(self, grid):
        answer = 0
        q=deque()
        r,c= len(grid),len(grid[0])

        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs():
            global answer
            while q :
                x,y=q.popleft()
                if grid[x][y]==1: 
                    grid[x][y]=0
                    for i in range (4):
                        dx=x+direction[i][0]
                        dy=y+direction[i][1]
                        if 0<=dx<r and 0<=dy<c :
                            if grid[dx][dy]==1:
                                q.append((dx,dy))
        def dfs2(count):
            global answer
            while q :
                x,y=q.popleft()
                if grid[x][y]==1: 
                    count+=1
                    grid[x][y]=0
                    for i in range (4):
                        dx=x+direction[i][0]
                        dy=y+direction[i][1]
                        if 0<=dx<r and 0<=dy<c :
                            if grid[dx][dy]==1:
                                q.append((dx,dy))
            return count
        for i in range(r):
            for j in range(c):
                if i==0 or i==r-1 :
                    if grid[i][j]==1:
                        q.append((i,j))
                        dfs()
                else :
                    if j==0 or j==c-1:
                        if grid[i][j]==1:
                            q.append((i,j))
                            dfs()
        print(grid)
        
        for i in range (1,r):
            for j in range(1,c):
                if grid[i][j]==1:
                    q.append((i,j))
                    answer+=dfs2(0)
        
        return answer
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # sum(x for x in arr) 요런 감성 까먹지 말자