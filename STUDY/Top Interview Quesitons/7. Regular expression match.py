class Solution(object):
    def isMatch(self, s, p):
        def rec(s,p):
            if not p and not s:
                return True
            if not p:
                return False
            pLen = len(p)
            sLen = len(s)
            if pLen > 1 and p[1] == '*':
                if rec(s, p[2:]) == True:
                    return True
                if sLen > 0 and (s[0] == p[0] or p[0]=="."):
                    return rec(s[1:],p)
            else:
                if sLen > 0 and (s[0]==p[0] or p[0]=='.'):
                    return rec(s[1:], p[1:])
            return False
        return rec(s,p)
        