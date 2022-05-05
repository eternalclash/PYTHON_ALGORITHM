# 5m22s
import heapq
N = int(input())
q=[]
for _ in range(N):
    heapq.heappush(q,int(input()))
sum=0
while len(q) > 1:
    x=heapq.heappop(q)
    y=heapq.heappop(q)
    sum+=x+y
    heapq.heappush(q,x+y)

print(sum)