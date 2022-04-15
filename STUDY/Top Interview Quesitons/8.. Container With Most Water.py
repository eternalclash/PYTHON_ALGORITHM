# 후 그리디로 하면 안풀리네 ,,,, 아마 투 포인터 사용해야 하는 것 같다
# class Solution(object):
#     def maxArea(self, height):
#         def findContainer(k):
#             left=0
#             i=k-1
#             j=k+1
#             right=0
#             rT=False
#             lT=False
#             while True:
#                 if i>=0:
#                     if height[i]>=height[k]:
#                         left=i
#                         lT=True
                        
#                 else:
#                     break
#                 i-=1
#             while True:
#                 if j<len(height):
#                     if height[j]>=height[k]:
#                         right=j
#                         rT=True

#                 else:
#                     break
#                 j+=1
#             if lT and rT :
#                 return max(abs(k-left),abs(k-right))
#             elif lT and not rT:
#                 return abs(k-left)
#             elif not lT and rT:
#                 return abs(k-right)
#             else:
#                 return -1
#         answer=0
#         for i in range (len(height)):
#             answer=max(answer,height[i]*findContainer(i))
#         return answer
# 투 포인터가 맞았다 leetcode는 투 포인터를 참 좋아하는 것 같다
class Solution(object):
    def maxArea(self, height):
        left, right , container = 0, len(height)-1, 0
        while left<right:
            container= max(container,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return container
            