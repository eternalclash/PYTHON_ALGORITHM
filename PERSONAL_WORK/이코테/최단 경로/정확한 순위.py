N,M = map(int,input().split())
INF = int(1e6)
graph=[[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j]=0
answer=0
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,N+1):
    count=0
    for j in range(1,N+1):
        if graph[i][j]!=INF or graph[j][i] != INF:
            count+=1
    if count == N:
        answer+=1
print(answer)
        
     