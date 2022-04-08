class Solution(object):
    def findCircleNum(self, isConnected):
        visit=set()
        def dfs(city):
            if city not in visit:
                visit.add(city)
                for i in range (len(isConnected[city])):
                    if isConnected[city][i] ==1 and i !=city:
                        dfs(i)
        count = 0
        for i in range (len(isConnected)):
            if i not in visit:
                count+=1
                dfs(i)
        
        return count
        
                        
                        