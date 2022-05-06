from collections import deque
N,K= map(int,input().split())
q=deque()
q.append(N)
count=0
visited=set()
def bfs() :
    count=0
    while len(q)>0:
        for _ in range(len(q)):
            x=q.popleft()
            if x==K:
                return count
            if 0<=x<=100000 and x not in visited:
                visited.add(x)
                q.append(x-1)
                q.append(x+1)
                q.append(x*2)
        count+=1

print(bfs())
