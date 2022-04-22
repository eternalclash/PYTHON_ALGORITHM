import math


T= int(input())

for i  in range (T):
    H,W,N = map(int,input().split())
    x=N%H*100
    if x==0:
        x=H*100
    y=math.ceil(N/H)
    print(str(x+y))