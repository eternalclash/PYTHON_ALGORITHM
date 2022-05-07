def solution(survey, choices):
    answer = ''
    def search_type(s,c):
        if c==4:
            return (s[i],0)
        if c-4>0:
            return (s[1],c-4)
        elif c-4<0:
            return (s[0],(c-4)*-1)
    obj={
        R:0,T:0,
        C:0,F:0,
        J:0,M:0,
        A:0,N:0
    }
    for i in range(len(survey)):
        x,y=search_type(survey[i],choices[i])
        obj[x]+=y
    

    if obj[R]>=obj[T]:
        answer+=R
    else:
        answer+=T
    if obj[C]>=obj[F]:
        answer+=C
    else:
        answer+=F
    if obj[J]>=obj[M]:
        answer+=J
    else:
        answer+=M
    if obj[A]>=obj[N]:
        answer+=A
    else:
        answer+=N
            



    return answer