# 정렬된 2차원함수에서 해당 숫자가 있는지 찾아라
# 누가봐도 이분 탐색이지만 너무 귀찮은걸~
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if i.count(target) >=1:
                return True
        return False
        