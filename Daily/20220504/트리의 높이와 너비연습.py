N=int(input())
graph=[[] for _ in range(N+1)] #트리구조 그리기
distance=[[] for _ in range(N+1)] #너비 찾기
is_root=[True for _ in range(N+1)] #루트노드 확인하기
root=0 #루트노드
for _ in range(N):
    node,left,right=map(int,input().split())
    graph[node].append(left)
    graph[node].append(right)
    if left!=-1:
        is_root[left]=False
    if right!=-1:
        is_root[right]=False

for i in range(1,N+1):
    if is_root[i]==True :
        root=i
        break

num=1 #너비의 인덱스 값을 표현
 #높이의 인덱스 값을 표현
def in_order(root,deep):
    global num
    if graph[root][0] != -1:
        in_order(graph[root][0],deep+1)
    distance[deep].append(num)
    num+=1
    if graph[root][1] != -1:
        in_order(graph[root][1],deep+1)
in_order(root,1)
answer=max(distance[1])-min(distance[1])+1
level=1
for i in range(1,N+1):
    if distance[i]:
        left=min(distance[i])
        right=max(distance[i])
        width=right-left+1
        if answer < width:
            answer=width
            level=i
print(level)
print(answer)



    