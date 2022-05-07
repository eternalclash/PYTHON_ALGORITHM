from collections import deque
import copy
def solution(queue1, queue2):

    q=queue1+queue2
    s=sum(q)
    q=sorted(q)
    print(q)
    if q[-1]>s-q[-1]:
        return -1
    
    
    count = 0
    sum_q1=sum(queue1)
    sum_q2=sum(queue2)
    queue1=deque(queue1)
    queue2=deque(queue2)
    while sum_q1 != s/2 and sum_q2 !=s/2:
        if sum_q1>sum_q2:
            x=queue1.popleft()
            queue2.append(x)
            sum_q1-=x
            sum_q2+=x
        elif sum_q1<sum_q2:
            x=queue2.popleft()
            queue1.append(x)
            sum_q2-=x
            sum_q1+=x
        count+=1
    return count


    

print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
