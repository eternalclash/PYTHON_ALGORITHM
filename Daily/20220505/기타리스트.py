
N,S,M= map(int,input().split())
dp=[[False]*(M+1) for _ in range(N+1)]
dp[0][S]=True
arr= list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(M+1):
        if dp[i][j]==True:
            if 0<=j+arr[i]<=M:
                dp[i+1][j+arr[i]]=True
            if 0<=j-arr[i]<=M:
                dp[i+1][j-arr[i]]=True
answer=-1
for i in range(M+1):
    if dp[N][i]==True:
        answer=i
print(answer)
