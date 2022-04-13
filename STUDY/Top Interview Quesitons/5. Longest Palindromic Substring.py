class Solution(object):
    def longestPalindrome(self, s):
        result=""
        for i in range(len(s)):
            l,r=i,i+1
            while 0<=l and r<len(s) and s[l]==s[r]:
                if len(result) < len(s[l:r+1]):
                    print(s[l:r+1])
                    result=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i
            while 0<=l and r<len(s) and s[l]==s[r]:
                if len(result) < len(s[l:r+1]):
                    print(s[l:r+1])
                    result=s[l:r+1]
                l-=1
                r+=1
        return result
                
        """
        :type s: str
        :rtype: str
        """
        