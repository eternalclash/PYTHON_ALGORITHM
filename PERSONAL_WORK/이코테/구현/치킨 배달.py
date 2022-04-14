## 이제 대충 풀 수 있는데 시간복잡도와 메모리 크기를 생각하자

from collections import deque
N,M = map(int,input().split()) #N은 판의 길이, M은 치킨 집 개수
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))





def combination(arr,n):
    result=[]
    if n==0 : return [[]]
    for i in range(len(arr)):
        fixed=arr[i]
        rest=arr[i+1:]
        for combi in combination(rest,n-1):
            result.append([fixed]+combi)
    return result

chicken =[]
home = []
direction= [(1,0),(0,1),(-1,0),(0,-1)]
def findmin (a,b):
    answer=0
    q=deque()
    q.append((a,b))
    while q:
        for _ in range(len(q)):
           x,y = q.popleft()
           if arr[x][y]==2:
              return answer
           for i in range(4):
               dx=x+direction[i][0]
               dy=y+direction[i][1]
               if 0<=dx<N and 0<=dy<N :
                   q.append((dx,dy))
        answer+=1

    return answer
        


for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]==2:
            chicken.append((i,j))
            arr[i][j]=0
        if arr[i][j]==1:
            home.append((i,j))
resultChicken= combination(chicken,M)

sol=99999999999
for result in resultChicken:
    res=0
    for a,b in home:
        sum=999999
        for x,y in result:
            sum=min(sum,abs(a-x)+abs(b-y))
        res+=sum
    sol=min(res,sol)
        


print(sol)
    

    
    
