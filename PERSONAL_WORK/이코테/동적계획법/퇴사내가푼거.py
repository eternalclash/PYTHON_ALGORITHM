n= int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([x,y,0])

for i in range(len(arr)):
    a=arr[i][0]
    b=arr[i][1]
    c=arr[i][2]
    if i+a<len(arr):
        if b>arr[i+a][2]:
            arr[i+a][2]=b+c
    elif i+a==len(arr):
        continue
    else:
        arr[i][1]=0
print(arr)
answer=0
for i in range(len(arr)):
    if arr[i][1]+arr[i][2]>answer:
        answer=arr[i][1]+arr[i][2]
print(answer)

    