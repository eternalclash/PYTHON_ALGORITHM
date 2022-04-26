for tc in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    x=0
    result=[]
    for i in range(n):
        k=arr[x:x+m]
        x+=m
        result.append(k)
    for j in range(1,m):
        for i in range(n):
            if i==0:
                left_up=0
            else:
                left_up=result[i-1][j-1]
            if i==n-1:
                left_down=0
            else:
                left_down=result[i+1][j-1]
        left=result[i][j-1]
        result[i][j]=result[i][j]+max(left,left_down,left_up)
    a=0
    for i in range(n):
        if result[i][m-1]>a:
            a=result[i][m-1]
    print(a)


    print(result)