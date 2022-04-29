class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums) + 1
        checkList = [False] * size
        
        for num in nums:
            if num >= 0 and num < size:
                checkList[num] = True
                
        for i in range(1, size):
            if checkList[i] == False:
                return i
            
        return size