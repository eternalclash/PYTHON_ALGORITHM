class Solution(object):
    def twoSum(self, nums, target):
        nums_map={}
        for i,num in enumerate(nums):
            nums_map[num]=i
        
        for i,num in enumerate(nums):
            if target - num in nums_map and i !=nums_map[target - num]:
                return [i,nums_map[target - num]]

# 객체에 값:인덱스 형식으로 넣은 다음 target에서 뺀 값을 바로 찾을 수 있게 한다
# 배열에서는 순회를 하면서 찾지만 객체에서는 직관적으로 찾을 수 있는게 포인트
# 또한 인덱스와 같이 넣을 수 있는 enumerate() 기억하자