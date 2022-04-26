import sys
n= int(input())
arr=[]
for _ in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    arr.append(data)

for i in range(1,len(arr)):
    for j in range(len(arr[i])):
        if j==0:
            top_left=0
        else:
            top_left=arr[i-1][j-1]
        if j==len(arr[i])-1:
            top_right=0
        else:
            top_right=arr[i-1][j]
        print(top_left,top_right)
        arr[i][j]=arr[i][j]+max(top_left,top_right)
answer=0
print(arr)
for i in range(len(arr[-1])):
    if arr[-1][i]>answer:
        answer=arr[-1][i]

print(answer)



