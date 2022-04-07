INF = int(1e9) # 무한을 의마하는 값으로 10억을 설정

n= int(input()) #노드의 개수
m= int(input()) #간선의 개수

#2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range( 1, n+1):
    for b in range(1, n+1):
        if a== b:
            graph[a][b]=0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b],end="")
    print()

# 노드의 개수 및 간선의 개수 입력받기
# 2차원 리스트(그래프) 노드의 개수만큼의 길이, 무한으로 초기화
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
# 점화식에 따라 플로이드 워셜 알고리즘 수행