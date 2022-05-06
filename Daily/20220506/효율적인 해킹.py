from collections import deque
N,M= map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    arr[y].append(x)

q=deque()
answer=0


def bfs(i):
    visited=set()
    visited.add(i)
    count=1
    while q:
        x=q.popleft()
        for y in arr[x]:
            if y not in visited:
                visited.add(y)
                q.append(y)
                count+=1
    return count
result=[]
for i in range(1,N+1):
    q.append(i)
    c = bfs(i)
    if c>answer:
        answer=c
        result=[i]
    elif c==answer:
        result.append(i)
        answer=c

for z in result:
    print(z,end=" ")




