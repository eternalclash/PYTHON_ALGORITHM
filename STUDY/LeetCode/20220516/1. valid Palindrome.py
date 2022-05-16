from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack=deque()
        for i in s:
            if i.isalnum():
                stack.append(i.lower())
        
        while len(stack) > 1:
            if stack.popleft() != stack.pop():
                return False
        return True
                
# deque의 popleft는 리스트의 pop(0)보다 빠르다 O(1)<O(N)
# isalnum,isalpha,isnum 문자,숫자 구별할 때에 필요한 메소드들
# python에서 문자열이 나오면 slicing을 기본으로 하자 제일 빠르기 떄문에
# str="abcde" str[::-1]="edcba", str[::2]="ace"