direction=[(-1,0),(0,-1),(1,0),(0,1)]

n,m = map(int,input().split())
d= [[0] * m for _ in range(n)]  #리스트라고 안 적어도 된다 [[0]*m for _ in range(n)]
x,y,di = map(int,input().split())
arr = []
for i in range (n):
    arr.append(map(int,input.split()))
time,count=0,0
while True :
    if di==3 : di= -1
    di=di+1
    dx= x+direction[di][0]
    dy= y+direction[di][1]
    if arr[dx][dy] == 0:
        d[x][y]==1
        x,y=dx,dy
        count+=1
    else :
        time +=1
        if time== 4:
            dx= x-direction[di][0]
            dy= y-direction[di][1]
            if d[dx][dy]==0:
                x,y=dx,dy
            else:
                break
            time = 0
print(count)


            

