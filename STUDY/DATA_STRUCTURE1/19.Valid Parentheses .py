class Solution(object):
    def isValid(self, s):
        stack =[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i] == "{":
                stack.append(s[i])
            else :
                if len(stack):
                    if s[i]=="]" and stack[-1]=="[":
                        stack.pop()
                    elif s[i]=="}" and stack[-1]=="{":
                        stack.pop()
                    elif s[i]==")" and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) > 0 : return False
        return True