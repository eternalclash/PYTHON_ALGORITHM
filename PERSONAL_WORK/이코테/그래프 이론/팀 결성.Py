N, M = map(int,input().split())
parents = [i for i in range(N+1)]

def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents,parents[x])
    return parents[x]

def union(parents,x,y):
    x=parents[x]
    y=parents[y]
    if x > y :
        parents[x]=y
    else :
        parents[y]=x

for _ in range(M):
    x,a,b= map(int,input().split())
    if x== 0:
        union(parents,a,b)
    if x== 1:
        if find_parents(parents,a)==find_parents(parents,b) :
            print("YES")
        else :
            print("NO")
