from collections import deque
N = int(input())
K = int(input())
apple=[]
for _ in range(K):
    x,y=map(int,input().split())
    apple.append((x,y))

L = int(input())
change = {}
for _ in range(L):
    x,y=input().split()
    change[int(x)]=y

# 배열 판 만들기
arr= [[0]*(N+1) for _ in range(N+1)]
direction= [(0,1),(1,0),(0,-1),(-1,0)]
# 사과의 위치 넣어주기
r=len(arr)
c=len(arr[0])
for (x,y) in apple:
    arr[x][y]=1

def turn(direction,c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction
snake=deque()
x,y=1,1
snake.append((1,1))
arr[x][y]=2
d = 0
time =0 

# 뱀 이동하기
while True :
    nx=x+direction[d][0]
    ny=y+direction[d][1]
    time +=1
    if 0<=nx<len(arr) and 0<=ny<len(arr) and arr[nx][ny] != 2:
        if arr[nx][ny] !=1:
            delX,delY=snake.popleft()
            arr[delX][delY]=0
        arr[nx][ny]=2
        snake.append((nx,ny))
        if time in change.keys():
            d=turn(d,change[time])
        
    else:
        break

print(time)




