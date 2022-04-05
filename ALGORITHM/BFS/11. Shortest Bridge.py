from collections import deque
def shortestBridge(self, grid):
    N = len(grid)
    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    visit=set()
    def invalid(x,y): # invalid == True 유효하지 않다
        return x<0 or y<0 or x==N or y==N
    def dfs(x,y):
          
        if (x<0 or y<0 or x==N or y==N or grid[x][y]==0 or (x,y) in visit):
            return
        visit.add((x,y))
        for dx,dy in direction:
            dfs(x+dx,y+dy)
        
    def bfs():
        res, q = 0, deque(visit)
        print(q)
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direction:
                    curR, curC = r+dr, c+dc
                       
                    if invalid(curR, curC) or (curR, curC) in visit:
                        print(curR,curC)
                        continue
                    if grid[curR][curC]:
                        return res
                    print("여기",curR,curC)
                    q.append((curR,curC))
                    visit.add((curR,curC))
            res +=1

    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                dfs(r,c)
                print (visit)
                return bfs()
print(shortestBridge(0,[[0,1],[1,0]]))
            