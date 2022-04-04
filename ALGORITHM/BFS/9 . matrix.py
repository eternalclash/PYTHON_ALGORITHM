from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        q=deque()
        row = len(mat)
        col = len(mat[0])
        for x in range(row):
            for y in range(col):
                if mat[x][y]==0:
                    q.append((x,y))
                else :
                    mat[x][y]=1100000000
        while q :
            x,y = q.popleft()
            for k in range(4):
                dx= x + direction[k][0]
                dy= y + direction[k][1]
                if 0<=dx<row and 0<=dy<col and mat[dx][dy]>mat[x][y]:
                    mat[dx][dy]=mat[x][y]+1
                    q.append((dx,dy))
        return mat
                