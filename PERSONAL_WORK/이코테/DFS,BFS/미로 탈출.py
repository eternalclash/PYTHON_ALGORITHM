from collections import deque
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

direction=[(1,0),(0,1),(-1,0),(0,-1)]
q= deque()
q.append((0,0))
def bfs():
    while(q):
        x,y=q.popleft()
        for i in range(4):
            dx=x+direction[i][0]
            dy=y+direction[i][1]
            if 0<=dx<n and 0<=dy<m:
                if arr[dx][dy]==1:
                    q.append((dx,dy))
                    arr[dx][dy]=arr[x][y]+1
bfs()
print (arr[n-1][m-1])
