array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    pivot=i
    for j in range(i+1,len(array)):
        if array[pivot] > array[j]:
            pivot=j
    array[i],array[pivot]=array[pivot],array[i]
print(array)
        