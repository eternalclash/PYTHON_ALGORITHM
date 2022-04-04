def pacificAtlantic(heights):
        
        rows= len(heights)
        columns = len(heights[0])
        atlantic=False
        pacific=False
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited= [[0]*columns for i in range(rows)]
        answer=[]
        s=[]
        def dfs(x,y,visited):
            visited[x][y]=1
            if x==0 or y==0 :
                answer.append(1)
               
            if x==rows-1 or y==columns-1:
                s.append(2)
                            
            for t in range(4):
                dx = x + direction[t][0]
                dy = y + direction[t][1]
                if 0<= dx < rows and 0<= dy < columns and heights[x][y]>=heights[dx][dy] and not visited[dx][dy]:
                    dfs(dx,dy,visited)
                    

            
        for k in range(5):
            for j in range(5):
                t=visited
                dfs(k,j,t)
                if len(answer)>0 and len(s)>0:
                    print(k,j)
                t=[]
                answer=[]
                s=[]
              
               
        return answer
print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
                