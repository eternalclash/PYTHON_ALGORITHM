#1. s[:]=s[::-1]이나 s.reverse()로 처리해도 되지만 투 포인터를 사용해서 해결

def solution(s):
    left,right=0,len(s)-1
    while right>left:
        s[left],s[right]=s[right],s[left]
        left +=1
        right +=1
    return s