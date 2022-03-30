class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                return True
        return False
# 무난무난 정렬 후 같은 숫자 있으면 TRUE 반복문을 다돌아도 없으면 FALSE