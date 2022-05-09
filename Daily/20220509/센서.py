import sys
N=int(input()) # 센서의 개수
M=int(input()) # 집중국의 개수
arr=list(map(int,input().split())) # 센서의 좌표
arr.sort()
answer=[]

if N<=M:
    print(0)
    sys.exit()

for i in  range (1,N):
    answer.append(arr[i]-arr[i-1])

answer=sorted(answer,reverse=True)

for i in range(M-1):
    answer[i]=0
print(sum(answer))
    
        


