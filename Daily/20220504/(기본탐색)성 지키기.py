# 11m 12s
# 완전 탐색에 딴생각 두지말자 시간반복도를 잘 계산하자
N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(input())

#세로 체크
count=0
for i in range(len(arr)):
    if arr[i].find('X')!=-1:
        continue
    else:
        count+=1

row_count=0
for j in range(M):
    sum=True
    for i in range(N):
        if arr[i][j]=="X":
            sum=False
            break
    if sum:
        row_count+=1
if row_count>count:
    print(row_count)
else:
    print(count)


            
    