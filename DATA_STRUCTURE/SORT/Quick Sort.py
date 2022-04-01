# Pivot => 큰 수와 작은 수를 교환할 때, 교환하기 위한 '기준' 피벗
# 전개 방법
# 1. 리스트에서 첫 번째 데이터를 피벗으로 정한다
# 2. 왼쪽에서 부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다, 그 다음 큰 데이터와 작은 데이터의 위치를 교환


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot=start
    left = start+1
    right = end
    while left <=right :
        while left <= end and array[left]<-array[pivot]:
            left +=1
        while right > start and array[right] >= array[pivot] :
            right -=1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        
        quick_sort(array, start, right - 1)
        quick_sort(array, right+1,end)