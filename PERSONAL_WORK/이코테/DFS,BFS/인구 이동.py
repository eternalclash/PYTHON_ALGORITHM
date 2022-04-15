from collections import deque
import copy

N,L,R = map(int, input().split())
arr =[]
for _ in range(N):
    sub=list(map(int,input().split()))
    arr.append(sub)

check=[]
visited=[[0]*N for _ in range(N)]

direction=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
    q=deque()
    q.append((i,j))
    stack=[]
    while q:
        for _ in range (len(q)):  
            x,y=q.popleft()
            if visited[x][y]==0:
                 stack.append((x,y))
            else:
                continue
            visited[x][y]=1
            for v in range(4):
                dx=x+direction[v][0]
                dy=y+direction[v][1]
                if 0<=dx<N and 0<=dy<N:
                    if L<=abs(arr[x][y]-arr[dx][dy])<=R and visited[dx][dy] ==0:
                        q.append((dx,dy))
    if len(stack)>0:
        check.append(copy.deepcopy(stack))
    
    
                    

    
    
time =0
while True:
    for i in range(N):
       for j in range(N):
           if not visited[i][j]:
             bfs(i,j)
    if len(check) == N*N:
        break
    for ch in check:
        sum=0
        for (x,y) in ch:
           sum+=arr[x][y]
        avg=int(sum/len(ch))
        for (x,y) in ch:
            arr[x][y]=avg
    check=[]
    visited=[[0]*N for _ in range(N)]
    time+=1

print(time)
