def isPalin(p):
    count=0
    for i in range(len(p)):
        if p[i]=="(":
            count+=1
        else:
            if count==0:
                return False
            count -=1
    return True

def equal(p):
    left,right=0,0
    for i in range(len(p)):
        if p[i] ==")":
            right+=1
        if p[i] =="(":
            left+=1
        if left==right:
            return i

def check(p):
    answer=''
    if p=='':
        return ''
    index=equal(p)
    u=p[:index+1]
    v=p[index+1:]
    if isPalin(u):
        answer=u+check(v)
    else:
        answer="("
        answer+=check(v)
        answer+=")"
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=")"
            else:
                u[i]='('
        answer+= "".join(u)
    return answer
        
    

def solution(p):
    return check(p)