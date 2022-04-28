import heapq

N = int(input())
INF=int(1e9)
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
distance=[[INF]*N for _ in range(N)]
q=[]
x,y=0,0
distance[x][y]=graph[x][y]
heapq.heappush(q,(graph[x][y],x,y))
direction=[(1,0),(0,1),(-1,0),(0,-1)]
while q:
    print(q)
    dist,x,y=heapq.heappop(q)
    if distance[x][y]<dist:
        continue

    for i in range(4):
        dx= x+direction[i][0]
        dy= y+direction[i][1]
        if 0<=dx<N and 0<=dy<N:
            cost=graph[dx][dy]+dist
            if cost<distance[dx][dy]:
                distance[dx][dy]=cost
                heapq.heappush(q,(cost,dx,dy))

print (distance)





