class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3=sorted(nums3)
        
        if len(nums3) % 2 !=0:
            return nums3[len(nums3)//2]
        else:
            if nums3[len(nums3)//2]+nums3[len(nums3)//2-1]==0: return 0 
            if (nums3[len(nums3)//2]+nums3[len(nums3)//2-1])%2 == 0: 
                return (nums3[len(nums3)//2]+nums3[len(nums3)//2-1])/2
            return (nums3[len(nums3)//2]+nums3[len(nums3)//2-1])/2+0.5 