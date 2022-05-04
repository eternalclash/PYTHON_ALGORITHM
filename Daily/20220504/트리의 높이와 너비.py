N=int(input())
graph=[[] for _ in range(N+1)] ## 그래프
isRoot = [False]*(N+1) ## 루트확인하는 리스트
distance= [[] for _ in range(N+1)] ## 거리값 저장하는 리스트
root=0
for _ in range(N):
    parent,left,right=map(int,input().split())
    graph[parent].append(left)
    graph[parent].append(right)
    isRoot[left]=True
    isRoot[right]=True

for i in range(1,N+1): #루트를 제외한 모든 점들은 2의 값을 가지기 때문에
    if isRoot[i]==False:
        root=i
        break
num=1
def inorder(start,deep): #deep은 레벨에 관련된 값, num은 거리에 관련된 값이다.
    global num
    if graph[start][0]!=-1:
        inorder(graph[start][0],deep+1)
    distance[deep].append(num)
    num+=1
    if graph[start][1]!=-1:
        inorder(graph[start][1],deep+1)

inorder(root,1)
level=1
answer=-99999
for i in range(1,N+1):
    if distance[i]:
        small=min(distance[i]) ## 각 층마다의 거리를 계산하여 최댓값인지 확인한다.
        large=max(distance[i])
        if answer<large-small+1:
            answer=large-small+1
            level=i
print(level)
print(answer)