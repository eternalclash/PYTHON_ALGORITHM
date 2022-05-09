# 2차원 배열 회전하는 건 이제 쉽죠~ 5m 24s
class Solution(object):
    def spiralOrder(self, matrix):
        answer=[]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(matrix)
        n=len(matrix[0])
        visited=set()
        x,y=0,0
        d=0
        def rotate90(d):
            if d >=3:
                d-=3
            else:
                d+=1
            return d
        while len(visited)<m*n:
            answer.append(matrix[x][y])
            visited.add((x,y))
            dx=x+direction[d][0]
            dy=y+direction[d][1]
            if 0<=dx<m and 0<=dy<n and (dx,dy) not in visited:
                x=dx
                y=dy
            else:
                d=rotate90(d)
                dx=x+direction[d][0]
                dy=y+direction[d][1]
                if 0<=dx<m and 0<=dy<n and(dx,dy) not in visited:
                    x=dx
                    y=dy
                else:
                    break
        return answer