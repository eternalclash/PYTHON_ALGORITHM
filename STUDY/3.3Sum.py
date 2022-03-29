# class Solution(object):
#     def threeSum(self, nums):
#         output=[]
#         def combination (arr, n) :
#             result = []
#             if n == 0 : return [[]]
#             for i in range(len(arr)):
#                 fixed = arr[i]
#                 restArr = arr[i+1:]
#                 for k in combination(restArr,n-1):
#                     result.append([fixed]+k)
#             return result
#         answer = combination(nums,3)
#         for ans in answer:
#             temp=sorted(ans)
#             ans = reduce(lambda x, y: x+y, ans)
#             if ans == 0:
#                 if temp not in output:
#                     output.append(temp)
             
#         return output
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []
        
        for i in range(len(nums)) :
            if i>0 and nums[i] == nums[i-1] : continue #중복일 때는 같은 숫자로 된 배열이 생길수도 있기때문에
            result = -nums[i]
            left =i+1
            right =len(nums)-1
            while right > left :
                if nums[left]+nums[right]<result:
                    left+=1
                elif nums[left]+nums[right]>result:
                    right-=1
                else:
                    answer.append((nums[i],nums[left],nums[right]))
                    left +=1
                    right -=1
        return set(answer)
    print(threeSum(3,[-1,-1,-1,0,1,1]))