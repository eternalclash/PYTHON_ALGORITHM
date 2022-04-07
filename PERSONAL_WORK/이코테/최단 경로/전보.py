import heapq
N,M,C = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
distances= [INF]*(N+1)
for _ in range (M):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start):
    queue=[]
    distances[start]=0
    heapq.heappush(queue,(distances[start],start))
    while queue:
        current_distance,current_node= heapq.heappop(queue)
        if distances[current_node] > current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance=weight+current_distance
            if distances[adjacent]>distance:
                distances[adjacent]=distance
                heapq.heappush(queue,(distance,adjacent))

dijkstra(C)
count =0
maxd=0
for i in range (1,N+1):
    if distances[i]==INF:
        continue
    else : 
        count+=1
        maxd.max(maxd,distances[i])

print(count-1,maxd)

