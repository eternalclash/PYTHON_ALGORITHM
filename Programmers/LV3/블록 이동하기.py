from collections import deque

def get_next_pos(pos,board):
    x1,y1,x2,y2=pos
    answer=[]
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(len(direction)):
        dx1=x1+direction[i][0]
        dy1=y1+direction[i][1]
        dx2=x2+direction[i][0]
        dy2=y2+direction[i][1]
        if board[dx1][dy1]==0 and board[dx2][dy2]==0:
            answer.append((dx1,dy1,dx2,dy2))
    if x1==x2:
        for i in [-1,1]:
            if board[x1+i][y1]==0 and board[x2+i][y2]==0:
                    answer.append((x1+i,y1,x1,y1))
                    answer.append((x2,y2,x2+i,y2))
    elif y1==y2:
        for i in [-1,1]:
            print(x1,y1,x2,y2)
            if board[x1][y1+i]==0 and board[x2][y2+i]==0:
                    answer.append((x1,y1+i,x1,y1))
                    answer.append((x2,y2,x2,y2+i))
    return answer
        
        

def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]
    q= deque()
    visited= []
    pos=(1,1,1,2)
    q.append((pos,0))
    visited.append(pos)
    
    while q:
        pos,cost = q.popleft()
        x1,y1,x2,y2=pos
        if (x1==n and y1==n) or (x2==n and y2==n):
            return cost
        for next_pos in get_next_pos(pos,new_board):
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)
    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))