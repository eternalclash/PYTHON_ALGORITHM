class Solution(object):
    def canVisitAllRooms(self, rooms):
        visit = set()
        def DFS (index):
            if index in visit:
                return
            visit.add(index)
            for room in rooms[index]:
                DFS(room)
        
        DFS(0)
        
        if len(visit) == len(rooms) : return True
        else : return False
            
            
        