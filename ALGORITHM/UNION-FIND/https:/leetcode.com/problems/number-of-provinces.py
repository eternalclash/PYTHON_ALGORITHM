def findCircleNum(isConnected):
    n = len(isConnected)  #n의 길이
    parent = [x for x in range(n)] #parent의 길이
    def find_parent(parent,x):
        if x != parent[x]:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]
    
    def union(parent,x,y):
        X=find_parent(parent,x)
        Y=find_parent(parent,y)
        if X < Y:
            parent[Y]=X
        else:
            parent[X]=Y
    
    for i in range (len(isConnected)):
        for j in range (len(isConnected[0])):
            if isConnected[i][j]:
                union(parent,i,j)
    answer=set(find_parent(parent,x) for x in parent)
    return len(answer)
print(findCircleNum([[1,0,0,0,1,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0],[0,1,0,1,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0],[1,0,0,0,0,1,1,0,1,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]]))



        