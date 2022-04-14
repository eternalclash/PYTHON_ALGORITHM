from collections import deque
N,K = map(int,input().split())
q= deque()
arr=[]
for i in range(N):
    sub=list(map(int,input().split()))
    arr.append(sub)
S,X,Y = map(int,input().split())
for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            q.append((arr[i][j],i,j))
q=sorted(q)
direction=[(1,0),(0,-1),(0,1),(-1,0)]
time=0
while time<S:
    for _ in range (len(q)):
        s,x,y=q.pop(0)
        for i in range(4):
            dx=x+direction[i][0]
            dy=y+direction[i][1]
            if 0<=dx<N and 0<=dy<N and arr[dx][dy]==0:
                arr[dx][dy]=s
                q.append((s,dx,dy))
    time+=1

if arr[X-1][Y-1]!=0: 
    print(arr[X-1][Y-1])
else:
    print(0)


