import sys
sys.setrecursionlimit(1000000)
T = int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    graph= [[0] * M for _ in range(N)] 
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    answer=0
    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x]=1
    def dfs(x,y):
        for i in range(4):
           dx=x+direction[i][0]
           dy=y+direction[i][1]
           if 0<=dx<N and 0<=dy<M and graph[dx][dy] == 1:
              graph[dx][dy]=0
              dfs(dx,dy)
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
               graph[i][j]=0
               answer+=1
               dfs(i,j)
    
    print(answer)
