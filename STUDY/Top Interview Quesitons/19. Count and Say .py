class Solution(object):
    def countAndSay(self, n):
        if n==1:
            return "1"
        x='1'
        test=""
        for i in range(n-1):
            count=1
            test=""
            for k in range(len(x)):
                if k != len(x)-1:
                    if x[k] ==x[k+1]:
                        count+=1
                    else:
                        test+=str(count)+str(x[k])
                        count=1
                else:
                    test+=str(count)+str(x[k])
            x=test
        return x