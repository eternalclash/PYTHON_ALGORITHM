
from urllib.parse import non_hierarchical


def count_by_value(array,x):
    n=len(array)
    a=first(array,x,0,n-1)
    print(a)
    if a== None:
        return 0
    b=last(array,x,0,n-1)
    print(b)
    if b== None:
        return 0
    return b-a+1

def first(array,target,start,end):
 
    if start>end:
        return None
    mid = (end+start)//2
    if (mid==0 or array[mid-1]>array[target]) and array[mid] == array[target]:
        return mid
    elif array[mid]<array[target]:
        return first(array,target,mid+1,end)
    else:
        return first(array,target,start,mid-1)
            
def last(array,target,start,end):
 
    if start>end:
        return None
    mid = int(end+start)//2
    if  (mid==len(array)-1 or array[mid+1]>target)  and array[mid] == target:
        return mid
    elif array[mid]<array[target]:
        return last(array,target,mid+1,end)
    else:
        return last(array,target,start,mid-1)
   


N,x = map(int,input().split())
array=list(map(int,input().split()))
count = count_by_value(array,x)

if count == 0:
    print(-1)
else:
    print(count)



