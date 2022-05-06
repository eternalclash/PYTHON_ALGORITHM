import heapq
T=int(input())
for _ in range(T):
    INF= int(1e9)
    N,D,C = map(int,input().split())
    arr=[[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for _ in range(D):
        a,b,s=map(int,input().split())
        arr[b].append((s,a))
    
    distance[C]=0
    q=[]
    heapq.heappush(q,(distance[C],C))
    while q :
        dist,x=heapq.heappop(q)
        if dist > distance[x]:
            continue
        for adj_dist,adj in arr[x]:
            total_dist=adj_dist+dist
            if distance[adj]>total_dist:
                distance[adj]=total_dist
                heapq.heappush(q,(total_dist,adj))
    answer=0
    count=0
    for i in range(1,N+1):
        if distance[i] != INF:
            answer=max(answer,distance[i])
            count+=1
    print(count, end=" ")
    print(answer)


    

    



