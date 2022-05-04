import heapq
#다익스트라로 풀면 좋을 것 같다는 생각이 들었다.
#최단 경로가 아닌 여럭 개의 경로중 최댓값을 구하는 것
#또한 경로끼리 더하는 것이 아닌 경로중 제일작은 값이 그 경로가 되는것
N,M= map(int,input().split())
INF = int(1e9)
arr=[[] for _ in range(N+1)]
distance=[0] * (N+1)
for _ in range(M):
    a,b,cost=map(int,input().split())
    arr[a].append((b,cost))
    arr[b].append((a,cost))

a,b= map(int,input().split())
q=[]
distance[a]=INF
heapq.heappush(q,(-distance[a],a))
while q:
    cost,x=heapq.heappop(q)
    cost=-cost
    if cost<distance[x]:
        continue
    for (y,d) in arr[x]:
        if distance[y]<min(d,cost):
            distance[y]=min(d,cost)
            heapq.heappush(q,(-distance[y],y))

print(distance[b])
