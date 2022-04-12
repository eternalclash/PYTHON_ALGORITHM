def solution(s):
    answer =99999999999
    if len(s)==1:
        return 1
    for i in range (1,len(s)//2+1):
        k=i
        stack=[]
        count=1
        while True:
            if i+k > len(s):
                if count > 1:
                    stack.append(str(count)+s[i-k:])
                else:
                    stack.append(s[i-k:])
                break
            if s[i-k:i]==s[i:i+k]:
                count+=1
            else:
                if count > 1:
                    stack.append(str(count)+s[i-k:i])
                    count=1
                else:
                    stack.append(s[i-k:i])  
            i+=k
        answer=min(answer,len("".join(stack)))
        stack=[]
            
        
    return answer