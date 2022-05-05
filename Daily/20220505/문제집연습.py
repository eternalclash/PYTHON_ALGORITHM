import heapq
N,M= map(int,input().split())
arr= [[] for _ in range(N+1)]
indegree= [0] * (N+1)
result=[]
q=[]
for _ in range(M):
    x,y=map(int,input().split())
    arr[x].append(y)
    indegree[y]+=1

for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(q,i)

while q :
    a=heapq.heappop(q)
    result.append(a)
    for e in arr[a]:
        indegree[e]-=1
        if indegree[e] == 0:
            heapq.heappush(q,e)

for i in result:
    print(i,end="")


