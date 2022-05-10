class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [True]+[False]*(len(nums)-1)
        for i in range (1,len(nums)):
            for j in range (i)[::-1]:
                if i-j<=nums[j] and dp[j]:
                    dp[i]=True
                    break
        
        return (dp[-1])