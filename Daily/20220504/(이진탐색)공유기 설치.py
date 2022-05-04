# 데이터의개수나 범위가 엄청 큰 경우에는 이진탐색을 고려할 만 하다
# 이진탐색은 재귀적이나 반복적으로 만들 수 있다.

n,c = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start=1
end=arr[-1]-arr[0]
while start<=end:
    mid=(start+end)//2
    count=1
    value=arr[0]
    for i in range(1,len(arr)):
        if arr[i]-value>=mid:
            value=arr[i]
            count+=1
    if count >=c:
        answer=mid
        start=mid+1
    else:
        end=mid-1

print(answer)
