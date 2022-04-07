#해시를 활용한 Union-Find 알고리즘 이용해 문제를 풀 수 있음 ,해시를 파이썬의 dictionary형을 활용해 사용
def find(x):
    if x==parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x]=p
        return parent[x]

def union (x,y):
    x = find(x)
    y = find(y)
    
    if x!=y:
        parent[y]= x
        number[x]+=number[y]
n= int(input())

for i in range(n):
    parent=dict()
    number=dict()
    m = int(input())
    for j in range(m):
        x,y=input().split()
        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1
        union(x,y)
        print(number[find(x)])





