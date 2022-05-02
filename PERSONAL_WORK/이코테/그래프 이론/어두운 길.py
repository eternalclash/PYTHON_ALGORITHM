def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x=parent[x]
    y=parent[y]
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v,e = map (int, input().split()) #노드의 개수와 간선의 개수 입력받기00
parent = [0] * (v+1) #노드의 개수에서 v+1하는 이유는 인덱스가 1부터 시작하므로

edges=[]
result = 0

for i in range(1,v+1):
    parent[i]= i
# 부모 초기화

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
total=0
for edge in edges:
    cost,a,b = edge
    total+=cost
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(total-result)