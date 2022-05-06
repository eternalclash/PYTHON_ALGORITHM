import math
##return을 생각하자
N,M = map(int,input().split())
arr=[]
for _ in range(N):
    x,y = map(int,input().split())
    arr.append((x,y))
already=[]
for _ in range(M):
    x,y=map(int,input().split())
    already.append((x,y))

def makeDistance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

distance=[]

for i in range(N):
    for j in range(i+1,N):
        distance.append((makeDistance(arr[i][0],arr[i][1],arr[j][0],arr[j][1]),i+1,j+1))
parent=[i for i in range(N+1)]
def find_parent(x):
    if parent[x] == x:
        return x
    return find_parent[x]

def union_find(x,y):
    x=find_parent(x)
    y=find_parent(y)
    if x < y:
        parent[y]=x
    elif x >y:
        parent[x]=y

for i in range(len(already)):
    x,y=already[i]
    union_find(x,y)

distance.sort()
answer=0
for cost,a,b in distance:
    if find_parent(a) != find_parent(b):
        union_find(a,b)
        answer+=cost

print("%0.2f" % answer)
