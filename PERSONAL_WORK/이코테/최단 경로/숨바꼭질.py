import heapq
N,M = map(int,input().split())
INF = int(1e6)
graph=[[] for _ in range(N+1)]
distance=[INF]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
distance[1]=0
q=[]
heapq.heappush(q,(1,distance[1]))
while q:
    x,dist=heapq.heappop(q)
    if dist>distance[x]:
        continue
    for d,cost in graph[x]:
        if distance[d] > cost+dist:
            distance[d]=cost+dist
            heapq.heappush(q,(d,distance[d]))

print(distance)
        
