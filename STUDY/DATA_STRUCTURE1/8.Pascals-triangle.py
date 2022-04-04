class Solution(object):
    def generate(self, numRows):
        arr=[[1],[1,1]]
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1],[1,1]]
        
        def Pascal (arr) :
            result =[]
            for i in range(len(arr)+1):
                if i == 0 or i==len(arr):
                    result.append(1)
                    continue
                result.append(arr[i-1]+arr[i])
            return result
        
        for k in range(numRows-2):
            arr.append(Pascal(arr[-1]))
        return arr