class Solution(object):
    def trap(self, height):
        left =0
        right = len(height)-1
        left_max,right_max=0,0
        answer=0
        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])
            
            if left_max <=right_max:
                answer+=left_max-height[left]
                left+=1
            else:
                answer+=right_max-height[right]
                right-=1
        return answer
                