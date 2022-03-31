# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range (len(nums)):
#             for j in range (i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
# 너무 쉬웠던 문제 속도가 다른 답보다 좀 늦었따 상위 60%정도?
# class Solution(object):
#        def twoSum(self, nums, target):
#         d = {}
#         for i, n in enumerate(nums):
#             m = target - n
#             print(i,n)
#             if m in d:
#                 return [d[m], i]
#             else:
#                 d[n] = i
# 이 답은 조금 더 빨랐지만 무엇보다 enumerate를 활용해서 풀어서 좋은 예시 인 거 같다
# 새로운 언어하는데 항상 문법 배제고릴라하니깐 언어에 대한 실력이 안 느는것 같다
arr =[2,5,3,1,4]
print(enumerate(arr)[0])