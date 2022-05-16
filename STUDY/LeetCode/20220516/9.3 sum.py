class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []
        
        for i in range(len(nums)) :
            if i>0 and nums[i] == nums[i-1] : continue #중복일 때는 같은 숫자로 된 배열이 생길수도 있기때문에
            result = -nums[i]
            left =i+1
            right =len(nums)-1
            while right > left :
                if nums[left]+nums[right]<result:
                    left+=1
                elif nums[left]+nums[right]>result:
                    right-=1
                else:
                    answer.append((nums[i],nums[left],nums[right]))
                    left +=1
                    right -=1
        return set(answer)

## set으로 해도 상관이 없다, 배열로 인식하나 보군
## 정렬 후 해당 인덱스 다음 인덱스 와 마지막 인덱스에서 투 포인터로 해결하면 된다