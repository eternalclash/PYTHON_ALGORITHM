row,col = map(int,input().split())
k=[]
for i in range(row):
    arr=list(map(int,input().split()))
    k.append(min(arr))
print(max(k))