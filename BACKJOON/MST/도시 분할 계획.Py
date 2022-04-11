


N,M = map(int,input().split())
parents = [i for i in range(N+1)]
edges=[]
for _ in range (M):
    a,b,c = map(int,input().split()) # a번집에서 b번집 길의 유지비 c
    edges.append((c,a,b))

def find_parents(parents,x):
    if parents[x] != x:
        parents[x]=find_parents(parents,parents[x])
    return parents[x]

def union(parents,x,y):
    x=find_parents(parents,x)
    y=find_parents(parents,y)
    if x > y:
        parents[x] = y
    else :
        parents[y] = x


edges.sort() # .sort() 이렇게 할 수 있다
result = 0
last = 0
for edge in edges:
    c,a,b= edge
    if find_parents(parents,a) != find_parents(parents,b):

        union(parents,a,b)
        result+=c
        last = c

print(result-last)
