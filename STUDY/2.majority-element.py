class Solution(object):
    def majorityElement(self, nums):
        obj ={}
        for num in nums:
            try:
                obj[num]+=1
            except KeyError :
                obj[num]=1
            if obj[num] > len(nums)/2 :
                return num