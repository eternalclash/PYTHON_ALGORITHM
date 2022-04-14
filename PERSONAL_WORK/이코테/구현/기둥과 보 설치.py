def solution(n, build_frame):
    def check(answer):
        for x,y,thing in answer:
            if thing == 0 : #기둥일 때
                if y==0 or (x,y-1,0) in answer or (x,y,1) in answer or (x-1,y,1) in answer:
                    continue
                else:
                    return False
            elif thing==1 : #보일 때
                if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer) :
                    continue
                else:
                    return False
        return True
    answer = []
    for i in range (len(build_frame)):
        x=build_frame[i][0]
        y=build_frame[i][1]
        thing=build_frame[i][2]
        setting=build_frame[i][3]
        if setting == 1:
            answer.append((x,y,thing))
            if not check(answer):
                answer.remove((x,y,thing))
        else :
            answer.remove((x,y,thing))
            if not check(answer):
                answer.append((x,y,thing))
    return sorted(answer)
            
            
                
            
            