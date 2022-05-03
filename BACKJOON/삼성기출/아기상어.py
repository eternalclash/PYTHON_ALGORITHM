# 이제 슬슬 준비가 되고 있는 것 같다
from collections import deque
N = int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
shark=deque()
shark_size=2
shark_count=0
fish = 1 # 1의 크기 물고기부터 탐색
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            shark.append((i,j))
            arr[i][j]=0
            break

visited_graph = [[False] * N for _ in range(N)]

direction = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(hunter_list,time):

    while shark:
        time +=1
        for _ in range (len(shark)):
            x,y=shark.popleft()
            for i in range(4):
                dx= x+direction[i][0]
                dy= y+direction[i][1]
                if 0<=dx<N and 0<=dy<N and arr[dx][dy]<=shark_size and not visited_graph[dx][dy]:
                    if 0<arr[dx][dy]<shark_size:
                        hunter_list.append([dx,dy,time])
                    shark.append((dx,dy))
                    visited_graph[dx][dy]=True
                    
   
    if len(hunter_list) == 0:
        return False
    hunter_list=sorted(hunter_list,key=lambda x : (x[2],x[0],x[1]))
    return hunter_list[0]


time=int(0)
shark_count=0
while True:
    result= bfs([],time)
    if result == False:
        break

    
    time=result[2]
    arr[result[0]][result[1]]=0
    shark.append((result[0],result[1]))
    shark_count+=1
    if shark_count == shark_size:
        shark_size+=1
        shark_count=0
    visited_graph = [[False] * N for _ in range(N)]
print(time)
    







