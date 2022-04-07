from collections import deque
class Solution(object):
    def allPathsSourceTarget(self, graph):
        q=deque()
        for i in graph[0] :
            q.append([0,i])
        
        def BFS ():
            answer=[]
            while q:
                
                arr=q.popleft()
                if arr[len(arr)-1]==len(graph)-1:
                    answer.append(arr)
                    continue
                for k in graph[arr[len(arr)-1]]:
                    q.append(arr+[k])
                
            return answer
        return BFS()
            