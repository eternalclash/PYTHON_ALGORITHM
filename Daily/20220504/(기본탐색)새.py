# 1 2 3 4 1 2 1

N=int(input())
count=0
i=1
while N>0:
    if N-i>=0:
        N-=i
        i+=1
        count+=1
    else:
        i=1
print(count)
