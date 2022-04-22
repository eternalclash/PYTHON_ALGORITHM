N = int(input())
answer=[]
five= N//5
k=0
while True:
   
    if N%5==0:
        print(k+N//5)
        break
    
    if N>=3:
        N-=3
        k+=1
    else:
        print(-1)
        break
    

