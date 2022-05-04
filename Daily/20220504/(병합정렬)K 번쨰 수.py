# 5m 55s
N,K = map(int,input().split())
arr=list(map(int,input().split()))
def merge_sort(arr) :
    if len(arr) ==1:
        return arr
    mid= len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else :
            arr[k]=right[j]
            k+=1
            j+=1
    
    if i==len(left):
        while j<len(right):
            arr[k]=right[j]
            k+=1
            j+=1
    elif j==len(right):
        while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
    
    return arr

answer=merge_sort(arr)
print(answer[K-1])
