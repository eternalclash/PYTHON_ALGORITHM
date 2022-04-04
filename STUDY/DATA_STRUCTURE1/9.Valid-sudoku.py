# 일일이 만드는 것 너무 귀찮아서 이런 유효성 중복 문제들은 역시 set으로 처리하면 쉽다
# 이 문제 풀고나서 좀 내 자신이 뿌듯했다 ㅋ

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