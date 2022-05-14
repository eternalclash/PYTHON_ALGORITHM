def solution(n, computers):
    parent = [x for x in range(n)]
    def find_parent(parent,x):
        if x==parent[x]:
            return parent[x]
        else:
            return parent[x]=find_parent(parent,parent[x])
    
    def union_parent(x,y):
        x=parent[x]
        y=parent[y]
        if x>y:
            parent[x]=y
        elif y>x:
            parent[y]=x
    
    for i in range (len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j]==1 and i != j and parent[i]!=parent[j]:
                union_parent(i,j)
                
    
    for i in range(len(parent)):
        find_parent(parent,i)
    return len(set(parent))
                
print(solution(4,[[1,0,1,1],[0,0,1,0],[1,1,0,0],[1,0,0,1]]))