n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(array,start,end,target):
    if start > end: return False
    mid=(end+start)//2
    if array[mid]<target:
        return binary_search(array,mid+1,end,target)
    elif array[mid]>target:
        return binary_search(array,start,mid-1,target)
    else:
        return True

for i in range(len(arr2)):
    print(binary_search(arr1,0,len(arr1)-1,arr2[i]))