#취약지점끼리의 거리가 짧은 곳부터 탐색
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak) #취약점의 길이
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start,start+length):
                if position < weak[index]:
                    count +=1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
            
    if answer > len(dist):
        return -1
    return answer