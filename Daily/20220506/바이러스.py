from collections import deque
q=deque()
N=int(input())
M=int(input())
arr=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

q.append(1)
visited= set()
def bfs():
    while q:
        x=q.popleft()
        if x not in visited:
            visited.add(x)
            
            for y in arr[x]:
                q.append(y)
bfs()
print(len(visited)-1)