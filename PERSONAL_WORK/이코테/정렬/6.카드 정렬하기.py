import heapq
from msilib.schema import ServiceControl
n= int(input())
arr=list( int(input())for _ in range(n))
heapq.heapify(arr)

answer = 0

while len(arr)  !=1:
    first=heapq.heappop(arr)
    second=heapq.heappop(arr)
    sum=first+second
    answer+=sum
    heapq.heappush(arr,sum)

print(answer)

