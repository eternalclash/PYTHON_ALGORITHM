S=input()
zero=0
one=0
for i in range(len(S)):
    if S[i] !=S[i-1]:
        if S[i-1]=="0":
            zero+=1
        else:
            one+=1
        if i==len(S)-1:
            if S[i]=="0":
                zero+=1
            else :
                one+=1
print(min(zero,one))

