class Solution(object):
    def longestPalindrome(self, s):
        def expand(s,left,right):

            while 0<=left and right <len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        result=''
        for i in range(len(s)):
            result=max(result,expand(s,i,i+1),expand(s,i,i),key=len)
        return result
            
            
## max를 이렇게 활용할 수 있구나 문자열의길이로 비교하교 문자열로 리턴 max(a,b,c,key=len)