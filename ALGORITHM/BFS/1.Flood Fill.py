# 기초적인 DFS 지정한 image[sr][sc]에서 인접한 상하좌우에서 같은 값들만 찾아주면 된다
# 예외처리에 유념하자

from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        q=deque()
        k = image[sr][sc]
        direction = [(0,1) ,(0,-1),(1,0),(-1,0)]
        q.append((sr,sc))
        if image[sr][sc]==newColor : return image
        def dfs():
            while q :
                x,y=q.popleft()
                if 0<=x<len(image) and 0<=y<len(image[0]):
                    if image[x][y]==k :
                        image[x][y]=newColor
                        for i in range(4):
                            dx=x+direction[i][0]
                            dy=y+direction[i][1]
                            q.append((dx,dy))
                       
        dfs()
        return image