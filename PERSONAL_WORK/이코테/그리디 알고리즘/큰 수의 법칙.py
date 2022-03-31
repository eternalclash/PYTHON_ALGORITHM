n,m,k= map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer =0
for i in range (1,m+1):
    if i%4 == 0 : answer+=arr[n-2]
    else : answer+=arr[n-1]

print(answer)

# 반복되는 패턴을 수학적으로 나누어서 구했으면O(1)도 가능함