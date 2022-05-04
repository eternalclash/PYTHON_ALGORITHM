# 아니 배열 하나로 어떻게 돌리냐고~ 32m43s 후~
# 너무 느리지만 뭐 풀었으니 OK~
class Solution(object):
    def rotate(self, matrix):
        l=0
        r=len(matrix)-1
        while l<r:
            matrix[l],matrix[r]=matrix[r],matrix[l]
            l+=1
            r-=1
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix

# 오른쪽으로 시계방향으로 돌리는 함수 

def rotate90(arr):
    answer=[[]*len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            answer[i][j]=arr[len(arr)-j-1][i]
    return answer