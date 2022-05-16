class Solution(object):
    def reorderLogFiles(self, logs):
        digit=[]
        letter=[]
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        return letter + digit
        """
        :type logs: List[str]
        :rtype: List[str]
        """
## lambda 활용의 중요성!!! 1순위,2순위를 표현할 떄 list형식으로 표현한다