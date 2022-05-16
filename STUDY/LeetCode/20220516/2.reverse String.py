class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left < right:
            s[left],s[right]=s[right],s[left]
            right-=1
            left+=1
        return s

# s.reverse(), s[::-1]로 풀어도 되는 문제
# 투 포인터의 개념을 활용함
# python swap : a,b=b,a 형식