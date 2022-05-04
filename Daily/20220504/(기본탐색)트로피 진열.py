# 12m30s
N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

max=-99999999
count=0
for i in range(0,len(arr)):
    if arr[i]>max:
        count+=1
        max=arr[i]
print(count)
max=-99999999
count=0
for i in range(len(arr)-1,-1,-1): ##역순으로 돌때는 중간에 -1로 둬야함 그래야 0까지 돔
    if arr[i]>max:
        count+=1
        max=arr[i]
print(count)
        

