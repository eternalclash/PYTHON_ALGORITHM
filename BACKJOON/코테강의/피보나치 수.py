def fibo(n):
    if n==0:
        return 0
    if n==2 or n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

x= int(input())

print(fibo(x))