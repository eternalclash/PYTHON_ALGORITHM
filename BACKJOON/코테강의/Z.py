N, r, c = map(int,input().split())
arr = [(2**N) * [0] for _ in range(2**N)]
direction=[(0,0),(0,1),(1,0),(1,1)]
def z(x,y):   
    answer=0
    for i in range (0,len(arr),2):
        for j in range (0,len(arr),2):
            for k in range (4):
                di=i+direction[k][0]
                dj=j+direction[k][1]
                answer+=1
                if x==di and y==dj:
                    return answer


    

           


print(z(r,c)-1)

    