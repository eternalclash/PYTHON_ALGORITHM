# 어제 2번에서 땅을 지나갈 때마다 1에서 0으로 바꾸는 과정에 +1연산을 통해 섬의 크기를 파악

class Solution(object):
    def maxAreaOfIsland(self, grid):
        def DFS(i,j,answer):
            if not grid[i][j]:
                return
            else:
                answer+=1
                grid[i][j]=0                           
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                    answer+=DFS(x,y,0)
            return answer
        max = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1 :
                    k = DFS(a,b,0)
                    if max < k : max=k
        
        return max
                