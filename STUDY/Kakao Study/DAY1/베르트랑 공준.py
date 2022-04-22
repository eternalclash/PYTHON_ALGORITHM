def find(num):
    if num==0 or num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
while True:
    N=int(input())
    if N==0:
        break
    x=0
    for i in range(N+1,2*N+1):
       if find(i):
          x+=1
    print(x)