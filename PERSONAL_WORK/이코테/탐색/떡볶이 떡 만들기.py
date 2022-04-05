n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr=sorted(arr)

def binary_search(start,end,target) :
    mid=(start+end)//2
    sum=0
    for i in range(len(arr)):
        if arr[i]>mid:
            sum+=arr[i]-mid
        else:
            continue
    if sum<m:
        end=mid-1
    else:
        result = mid
        start = mid+1