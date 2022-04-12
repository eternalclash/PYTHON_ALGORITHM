import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    s=0
    previous=0
    length = len(q)
    while s+ (q[0][0]-previous) * length < k:
        now=heapq.heappop(q)[0]
        s+=(now-previous)*length
        length-=1
        previous=now
    result = sorted(q,key=lambda x: x[1])
    return result[(k-s) % length][1]
        
        
print(solution([3,1,2],5))