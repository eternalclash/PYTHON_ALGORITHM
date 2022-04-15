from itertools import combinations
N =int(input())
arr=[]
for _ in range(N):
    sub=list(map(str,input().split()))
    arr.append(sub)
make=[]
teacher=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=="X":
            make.append((i,j))
        if arr[i][j]=="T":
            teacher.append((i,j))

makeobs=list(combinations(make,3))
direction=[(-1,0),(0,1),(1,0),(0,-1)]
find="NO"
def dfs(x,y,mode):
    if mode==0:
        while y<N:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            y+=1
    if mode==1:
        while y>=0:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            y-=1
    if mode==2:
        while x<N:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            x+=1
    if mode==3:
        while x>=0:
            if arr[x][y]=='S':
                return True
            if arr[x][y]=='O':
                return False
            x-=1
    return False

def teacherCheck(): #찾았다면 True 못찾으면 False
    for x,y in teacher:
        for i in range(4):
            if dfs(x,y,i):
                return True
    return False
    


for obs in combinations(make,3):

    for i in range (len(obs)):
        a,b=obs[i]
        arr[a][b]="O"
    if not teacherCheck():
        find="YES"
        break
    for i in range (len(obs)):
        a,b=obs[i]
        arr[a][b]="X"


print(find)




