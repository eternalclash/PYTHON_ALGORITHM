
# 예외처리 잘 생각하자
# 투 포인터 활용해서 해결
class Solution(object):
    def maxSubArray(self, nums):
        #배열의 길이가 1개
        if len(nums)==1:
            return nums[0]
        #배열이 모두 음수일 때
        for i in range(len(nums)) :
            if nums[i] >=0:
                break
            else:
                if i==len(nums)-1:
                    return max(nums)
        sum=0
        result=0
        #배열에 0 이상인 원소가 있을 때
        for i in range(len(nums)):
            now=nums[i]
            sum=max(now,sum+nums[i])
            if (sum<0):
                sum=0
            result=max(sum,result)
        return result