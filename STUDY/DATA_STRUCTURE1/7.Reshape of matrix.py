# 주말에 너무 쉬었나,,,
# mat에 있는 걸 1차원 배열로 만들고 그걸 다시 2차원배열로 만들기 이 문제는 자주 풀면 좋겠다 구현 능력많이 늘 듯

class Solution(object):
    def matrixReshape(self, mat, r, c):
        arr=[]
        for row in mat:
            for col in row:
                arr.append(col)
        
        if len(arr)!=r*c:
            return mat
        answer=[]
        for i in range(r):
            result = []
            for j in range(c):
                result.append(arr.pop(0))
            answer.append(result)
        return answer
            
                