class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

#파이썬 문자열은 너무나도 편안하다 푸근해~