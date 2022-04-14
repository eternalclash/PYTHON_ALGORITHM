from itertools import combinations
from collections import deque
import copy
N,M = map(int,input().split())
arr =[]
z= deque()
for _ in range(N):
    sub=list(map(int,input().split()))
    arr.append(sub)

wall=[]
direction=[(1,0),(-1,0),(0,1),(0,-1)]
for i in range (N):
    for j in range(M):
        if arr[i][j]==0:
            wall.append([i,j])
        if arr[i][j]==2:
            z.append((i,j))

threewall=list(combinations(wall,3))
def bfs ():
    s=copy.deepcopy(arr)
    q=deque(z)
   
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                dx= x+direction[i][0]
                dy= y+direction[i][1]
                if 0<=dx<N and 0<=dy<M and s[dx][dy]==0:
                    s[dx][dy]=2
                    q.append((dx,dy))
    return s    
answer=0
for walls in threewall:
    for w in walls:
        arr[w[0]][w[1]]=1
   
    
    sum=0
    
    for k in bfs():
        sum+=k.count(0)
    
    answer=max(answer,sum)

    for w in walls:
        arr[w[0]][w[1]]=0

print(answer)


