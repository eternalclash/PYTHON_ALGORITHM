#binary search는 푸근하네
from bisect import bisect_left,bisect_right
class Solution(object):
    def searchRange(self, nums, target):
        def first(target,start,end):
            mid = (start+end)//2
            if start>end:
                return -1
            if nums[mid]==target and (nums[mid]>nums[mid-1] or mid==0):
                return mid
            if nums[mid]==target and nums[mid]==nums[mid-1]:
                return first(target,start,end-1)
            if nums[mid]>target:
                return first(target,start,mid-1)
            if nums[mid]<target:
                return first(target,mid+1,end)
        def last(target,start,end):
            mid = (start+end)//2
            if start>end:
                return -1
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid]<nums[mid+1]):
                return mid
            if nums[mid]==target and nums[mid]==nums[mid+1]:
                return last(target,start,end+1)
            if nums[mid]>target:
                return last(target,start,mid-1)
            if nums[mid]<target:
                return last(target,mid+1,end)
        return [first(target,0,len(nums)-1),last(target,0,len(nums)-1)]
         