import heapq
def solution(n, paths, gates, summits):
    INF=int(1e9)
    distance= [0]*(n+1)
    graph= [[] for _ in range(n+1)]
    for path in paths:
        graph[path[0]].append((path[2],path[1]))
        graph[path[1]].append((path[2],path[0]))
    q=[]

    def dijkstra(start,distance):
        visited=set()
        distance[start]=0
        visited.add(start)
        heapq.heappush(q,(distance[start],start))
        while q :
            cost,t=heapq.heappop(q)
            if distance[t] > cost:
                continue
            for adj_cost,adj_t in graph[t]:
                if adj_t not in visited:
                    visited.add(adj_t)
                    if adj_t in gates:
                       continue
                    if distance[adj_t]<max(cost,adj_cost):
                       distance[adj_t]=max(cost,adj_cost)
                       heapq.heappush(q,(distance[adj_t],adj_t))
    dijkstra(gates[0],distance)
    print(distance)
        


    answer = []
    return answer
print (solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1]
, [5, 6, 1]],[1, 3],[5]))