# 다시 풀었는데 다 까먹었다,,
class Solution(object):
    def isValidSudoku(self, board):
        s = set()
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != ".":
                    if (col, i) in s or (j, col) in s or (i // 3, j // 3, col) in s:
                        return False
                    s.add((col, i))
                    s.add((j, col))
                    s.add((i // 3, j // 3, col))
        return True