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

# num=10  num의 제곱근은 3.xxx num의 탐색 범위는 2부터 4까지
# num에 대한 약수가 있을 때 약수 쌍이(x,y) 둘 중 하나의 약수는 무조건 제곱근이하 
# num=16 약수가 (1,16) , (2,8), (4)