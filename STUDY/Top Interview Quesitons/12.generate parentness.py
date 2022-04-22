import copy
class Solution(object):
    def generateParenthesis(self, n):
        answer=[]
        def parent(left,right,s,stack):
            if left==0 and right==0: 
                return answer.append(s)
            if left>0:     
                parent(left-1,right,s+"(",stack)
            if  right>left :
          
                parent(left,right-1,s+")",stack)
        parent(n,n,"",[])
        return answer
                