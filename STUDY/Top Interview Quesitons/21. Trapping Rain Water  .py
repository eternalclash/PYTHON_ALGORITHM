class Solution:
# @param A, a list of integers
# @return an integer
    def trap(self, arr):
        height, left, right, water = [], 0, 0, 0
        for i in arr:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(arr)):
            right = max(right, i)
            water += min(height[n], right) - i
        return water
