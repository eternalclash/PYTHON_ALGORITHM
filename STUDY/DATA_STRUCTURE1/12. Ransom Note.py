# 카운터로 다 추출하고 배열로 순회한다!
# 전 문제랑 비슷한 유형
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c1=Counter(ransomNote)
        c2=Counter(magazine)
        for r in ransomNote:
            if c2[r]>=c1[r]:
                continue
            else:
                return False
        
        return True
        
        