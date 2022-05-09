# 정렬 판단이 중요했던 문제
N= int(input())
c= list(map(int,input().split()))
M= int(input())
b = list(map(int,input().split()))
count=0
c.sort()
b=sorted(b,reverse=True)
if b[0] > c[-1]:
    print(-1)
else:
    while b:
        for i in range(len(c)):
            for j in range(len(b)):
                if c[i]>=b[j]:
                    del b[j]
                    break
        count+=1
    print(count)

