# 위상정렬 -> 힘 자료구조를 사용하면 효과적으로 풀 수 있음
# 위상정렬은 순서가 정해져 있는 작업을 차례로 수행해야 할 때 , 순서를 결정해줌
# 시간복잡도 O(V+E)
# 위상 정렬 순서
# 1. 진입 차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 3. 제거 이후에 진입 차수가 0이 된 정점을 귴에 삽입
# 4. 큐가 빌 때까지 2-3 과정 반복 
# 만약 모든 원소 방문하기 전에 큐가 빈다면 사이클이 존재
# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과
import heapq
n,m= map(int,input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)

heap=[]
result=[]
## 진입차수 늘리기
for _ in range(m):
    x, y = map(int,input().split())
    array[x].append(y)
    indegree[y] +=1

## indegree에서 0인 애들 힙에 넣기
for i in range (1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)

## 힙에서 애들 빼면서 거기에 할당되는 인덱스들 -1하고 돌리기
while heap:
    data=heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y]-=1
        if indegree[y]==0:
            heapq.heappush(heap,y)

for i in result:
    print(i, end=" ")