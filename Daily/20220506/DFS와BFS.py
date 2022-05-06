from collections import deque
N,M,V = map(int,input().split())
arr=[[] for _ in range(N+1)]
visited=[False] * (N+1)
visited_two=[False]*(N+1)
for i in range(M):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
q=deque()
for i in range(1,N+1):
    arr[i].sort()

def dfs(x):
    if not visited[x]:
        visited[x]=True
        print(x,end=' ')
    else:
        return
    for y in arr[x]:
        dfs(y)
q.append(V)
def bfs():
    while q:
        x=q.popleft()
        if not visited_two[x]:
            visited_two[x]=True
            print(x, end=" ")
            for y in arr[x]:
                q.append(y)


dfs(V)
print()
bfs()



    

