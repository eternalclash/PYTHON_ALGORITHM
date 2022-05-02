n,m= map(int,input().split())
arr=[]
for _ in range(n):
    s=list(map(int,input().split()))
    arr.append(s)

parent= [ i for i in range(n)]

def find_parent(x):
    if x==parent[x]:
        return x
    else:
        return find_parent(parent[x])

def union(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]==1:
            union(i,j)

plan = list(map(int,input().split()))

result = True
for i in range(m-1):
    if find_parent(plan[i]-1) != find_parent(plan[i+1]-1):
        result = False

if result:
    print("YES")
else:
    print("NO")

print(parent)