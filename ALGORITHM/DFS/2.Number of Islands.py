# 아이디어는 이차원 배열을 순회하면서 1인 즉 섬인 값이 있을 떄 DFS 시작
# DFS에서 1인 값을 탐색하면서 찾은 1인 값들을 0으로 처리 강으로 만들어버림
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        q=deque()
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        answer=0
        def dfs():
            while q:
                x,y=q.popleft()
                if 0<=x<len(grid) and 0<=y<len(grid[0]):
                    if grid[x][y] =="1":
                        grid[x][y]="0"
                        for i in range(4):
                            dx= x+direction[i][0]
                            dy= y+direction[i][1]
                            q.append((dx,dy))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1" :
                    q.append((i,j))
                    dfs()
                    answer+=1
        return answer
            