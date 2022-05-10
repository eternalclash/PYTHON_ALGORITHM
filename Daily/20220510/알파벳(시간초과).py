import sys
import copy
N,M= map(int,input().split())

arr=[]
for _ in range(N):
    a=list(sys.stdin.readline().rstrip())
    arr.append(a)

answer=[]
def dfs(x,y,stack):
    if x+1<N and arr[x+1][y] not in stack:
        stack.append(arr[x+1][y])
        dfs(x+1,y,stack)
        stack.pop()
    if 0<=x-1 and arr[x-1][y] not in stack:
        stack.append(arr[x-1][y])
        dfs(x-1,y,stack)
        stack.pop()
    

    
    if y+1<M and arr[x][y+1] not in stack:
        stack.append(arr[x][y+1])
        dfs(x,y+1,stack)
        stack.pop()
    
    if 0<=y-1 and arr[x][y-1] not in stack:
        stack.append(arr[x][y-1])
        dfs(x,y-1,stack)
        stack.pop()

  
    answer.append(copy.deepcopy(len(stack)))
dfs(0,0,[arr[0][0]])
print(max(answer))
