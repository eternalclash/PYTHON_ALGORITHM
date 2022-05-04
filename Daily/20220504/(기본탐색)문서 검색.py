# 4m 45s
# while문에서 나가는 제한 조건 확실히 두자
S=input()
P=input()
k=len(P)
i=0
answer=0
while i<len(S):
    if S[i:i+len(P)]==P:
        answer+=1
        i=i+len(P)
    else:
        i+=1

print(answer)
