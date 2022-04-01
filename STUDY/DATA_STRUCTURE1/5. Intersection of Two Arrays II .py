
#속도가 너무 느리다
class Solution(object):
    def intersect(self, nums1, nums2):
        answer=[]
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                if nums1[i]==nums2[j]:
                    answer.append(nums1[i])
                    del nums2[j]
                    break
        return answer

#양심에 찔려서,,,다시 풀었다,,,,,,배제하고 싶었는디
#counter라는 꿀 라이브러리가 있는지도 모르고 또 함수로 만들었네~

class Solution(object):
    def intersect(self, nums1, nums2):
        obj={}
        arr= []
        def count (obj,n,nums):
            for i in range(n):
                try:
                    obj[nums[i]]+=1
                except :
                    obj[nums[i]]=1
        count(obj,len(nums1),nums1)
        for num in nums2:
            if num in obj and obj[num]>0:
                arr.append(num)
                obj[num]-=1
        return arr
        
         
       
        