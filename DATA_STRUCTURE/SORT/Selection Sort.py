array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index],array[i]

#제일 낮은 숫자를 찾아서 앞으로 계속 보냄
# O**2/n
# 다른 정렬에 비해 비효율적이지만 특정한 리스트에서 가장 작은데이터를차즌 일이태반