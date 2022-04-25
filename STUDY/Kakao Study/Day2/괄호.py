T= int(input())
for _ in range(T):
    answer=0
    t=True
    n=input()
    for i in range(len(n)):
        if n[i]=="(":
            answer+=1
        else:
            if answer>0:
                answer-=1
            else:
                t=False
                break
    if not t: 
        print("NO")
    else:
        if answer>0:
            print("NO")
        elif answer==0:
            print("YES")




