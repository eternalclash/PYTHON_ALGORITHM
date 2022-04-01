
# n,m= map(int,input().split())

# answer=0
# arr = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# direction = [(0,1),(0,-1),(1,0),(-1,0)]
# def dfs(x,y):
#     global answer
#     if arr[x][y]==1:
#         answer+=1
#         arr[x][y]=0
#         for k in range(4):
#            dx=x+direction[k][0]
#            dy=y+direction[k][1]
#            if 0<=dx<n and 0<=dy<m:
#               dfs(dx,dy)
        


# for i in range(n):
#     for j in range(m):
#         if arr[i][j]==1:
#             dfs(i,j)
            

# print(answer)
def k(a):
    a.append(4)
b=[]
b=k(b)
print(b)