# 풀긴 풀었는데 계속 출제자의 의도를 벗어나게 푸는거 같다
# 속도도 너무 느리다 상위 80%,,,

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range (len(nums1)-m):
            nums1.pop()
        for i in range (n) :
            nums1.append(nums2.pop(0))
        return nums1.sort()


##투 포인터 활용한 답
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
# 좋은 답이긴 하지만 아이디어를 생각하지 못하면 이렇게 못 풀 것 같다