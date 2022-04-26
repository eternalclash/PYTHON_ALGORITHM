# 1. 각 단어를 길이에 따라서 나눈다.
# 2. 모든 리스트를 정렬한 뒤에, 각 쿼리에 대해서 이진 탐색 수행하여 문제를 해결 할 수 있다
# 3. bisect를 사용해서 푼다 bisect_left를 하면 중복된 수중에 왼쪽부터, bisect_right를 하면 중복된 수중에 오른쪽부터 실행된다

from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value):
    right_index= bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index

array=[[] for _ in range(10001)]

reversed_array=[[] for _ in range(100001)]

def solution(words,queries):
    answer=[]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?','a'),q.replace('?','z'))
        else:
            res= count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        answer.append(res)
    return answer
