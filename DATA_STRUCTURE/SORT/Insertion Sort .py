array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] <array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)
#최악은 O(N**2) 하지만 최선의 경우 O(N) 정렬이 거의 되어있는 상태에서 사용하는 것이 좋다

##배열의 두번째 요소부터 끝까지 순회하면서 함
# 전의 요소와 비교하여 전의요소보다 크면 break
# 전의 요소와 비교하여 작으면 둘의 순서를 바꾼다