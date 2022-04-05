from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        n,m= len(maze),len(maze[0])
        exit=set()
        visit=set()
        direction=[(1,0),(0,1),(0,-1),(-1,0)]
        for i in range(n):
            for j in range(m):
                if entrance[0]==i and entrance[1]==j: continue #entrance가 exit인 경우 제외
                if i==0 or i==n-1:
                    exit.add((i,j))
                elif j==0 or j==m-1:
                    exit.add((i,j))
        # exit 테두리 완성
        def invalid(r,c):
            return r<0 or c<0 or r==n or c==m
        
        def BFS():
            res=0
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
               
                    visit.add((x,y))
                    if (x,y) in exit: 

                        return res
                    for i in range(len(direction)):
                        dx= x+direction[i][0]
                        dy= y+direction[i][1] 
                        if not invalid(dx,dy) and maze[dx][dy]=="." and (dx,dy) not in visit:
                            q.append((dx,dy))
                res+=1
            return -1
                    
                
                

        q=deque()
        q.append(entrance)
        return BFS()