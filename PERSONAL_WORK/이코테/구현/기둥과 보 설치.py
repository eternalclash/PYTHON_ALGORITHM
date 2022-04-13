def solution(n, build_frame):
    answer=[[]]
    for i in range(len(build_frame)):
        x,y=build_frame[i][0],build_frame[i][1]
        settle=build_frame[i][2]
        think=build_frame[i][3]
        if think==1: #설치
            if settle == 0: # 기둥일 떄
                if y==0 or (x,y-1,0) in answer or (x,y,1) in answer or (x-1,y,1) in answer:
                    answer.append((x,y,0))
                else:
                    continue
            else : # 보일 때
                if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                    answer.append(x,y,1)
                else:
                    continue
        else: #삭제 
            if settle == 0: #기둥일 때
                if 
                     
                
            
            