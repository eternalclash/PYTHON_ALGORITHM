# class Solution(object):
#     def firstUniqChar(self, s):
#         for i in range (len(s)):
#             if s.count(s[i]) == 1: return i
#         return -1

#이건 너무 양심없는 코드 O(N**2)이므로 너무 느리다
class Solution(object):
    def firstUniqChar(self, s):
        obj={}
        for i in range (len(s)):
            try :
                obj[s[i]]+=1
            except KeyError:
                obj[s[i]]=1
        
        for i in range(len(s)):
            if obj[s[i]]==1:
                return i
        
        return -1
# 객체 활용해서 찾음~~