# 1 2 3 4 5
import math
# 1 1 2 3 5
N=int(input())
arr=[int(input()) for _ in range(N)]
arr.sort()
test=[i+1 for i in range(N)]
answer=0
for i in range(N):
    if arr[i]!=test[i]:
        answer+=abs(arr[i]-test[i])
print(answer)

