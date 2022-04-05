from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        i = Counter(s)
        j = Counter(t)
        if len(s)>len(t):
            for k in s:
                if i[k] == j[k]: 
                    continue
                else:
                    return False
        else:
            for k in t:
                if i[k] == j[k]:
                    continue
                else:
                    return False
        return True
        