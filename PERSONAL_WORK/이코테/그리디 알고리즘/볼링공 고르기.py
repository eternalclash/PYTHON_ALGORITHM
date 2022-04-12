N,M= map(int,input().split())
result=0
arr=list(map(int,input().split()))
for i in range(N):
    for j in range(i+1,N):
        if arr[i]==arr[j]:
            continue
        else:
            result+=1

print(result)
