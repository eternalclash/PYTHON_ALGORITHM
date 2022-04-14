from collections import deque
N,M,K,X = map(int,input().split())
arr= [[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    arr[x].append(y)

distance=[0]*(N+1)
# K 거리 정보, X는 출발 도시의 번호

def bfs(X):
    q= deque()
    q.append(X)
    k=1
    while q:
        for z in range(len(q)):
            d= q.popleft()
            for index in arr[d]:
                if distance[index] == 0 and index!=X:
                    distance[index]+=k
                    q.append(index)
                 
        k+=1

bfs(X)

if distance.count(K) == 0 : print(-1)
for i in range(1,N+1):
    if distance[i]==K:
        print(i)
        

