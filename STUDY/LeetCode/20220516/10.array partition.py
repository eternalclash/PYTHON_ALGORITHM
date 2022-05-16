class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
# pythonic 하다