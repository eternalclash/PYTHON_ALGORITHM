from collections import deque

# 테스트 케이스만큼 반복
for tc in range(int(input())):
    # 노드의 개수 입력받기
    n=int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기호ㅓ
    indegree=[0]*(n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph=[[False]*(n+1)for i in range(n+1)]
    # 작년 순위 정보 입력
    data = list(map(int,input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]]=True
            indegree[data[j]] +=1
    # 올해 변경된 순위 정보입력
    m= int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -=1
            indegree[b] +=1
    result = []
    q= deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    certain= True
    cycle= False
    
    for i in range(n):
        if len(q) == 0:
            cycle=True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -=1
                if indegree[j] == 0:
                    q.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i,end=' ')
        print()