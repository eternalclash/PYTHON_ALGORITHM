class Solution(object):
    def merge(self, intervals):
        answer=[]
        intervals.sort()
        if len(intervals) ==1:
            return intervals
        for i in range(len(intervals)-1):
            if i+1==len(intervals)-1:
                if intervals[i][1]>=intervals[i+1][0]:
                    intervals[i+1]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
                    answer.append(intervals[i+1])
                else:
                    answer.append(intervals[i])
                    answer.append(intervals[i+1])
                break
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
            else:
                answer.append(intervals[i])
        return answer
                
                
            
        