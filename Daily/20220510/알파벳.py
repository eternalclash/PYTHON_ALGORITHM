

N,C = map(int,input().split())
arr= []
for _ in range(N):
    arr.append(input())
direction=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):
    global result
    q= set()
    q.add((x,y,arr[x][y]))

    while q:
        x,y,step = q.pop()
        result = max(result,len(step))

        for i in range(4):
            dx= x+direction[i][0]
            dy= y+direction[i][1]

            if 0<=dx<N and 0<=dy<C and arr[dx][dy] not in step:
                q.add((dx,dy,step+arr[dx][dy])) # 포인트 파이썬만 가능한 운영 원래는 넣고 뺴야함
        
result = 0
bfs(0,0)
print(result)