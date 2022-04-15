import copy
N= int(input())
nums=list(map(int,input().split()))
op=list(map(int,input().split()))
oparr=[]
def dfs(a,b,c,d,arr):
    if a==0 and b==0 and c==0 and d==0:
        oparr.append(copy.deepcopy(arr))
        return

    if a>0:
        arr.append("+")
        dfs(a-1,b,c,d,arr)
        arr.pop()
    if b>0:
        arr.append("-")
        dfs(a,b-1,c,d,arr)
        arr.pop()
    if c>0:
        arr.append("*")
        dfs(a,b,c-1,d,arr)
        arr.pop()
    if d>0:
        arr.append("/")
        dfs(a,b,c,d-1,arr)
        arr.pop()

dfs(op[0],op[1],op[2],op[3],[])
high=-999999999999
low=99999999999999
for operator in oparr:
    sum=str(nums[0])
    for i in range(len(operator)):
        if operator[i]=="/":
            sum=eval(sum+operator[i]+str(nums[i+1]))
            sum=int(sum)
          

        else:
            sum=eval(sum+operator[i]+str(nums[i+1]))
        sum=str(sum)
    high=max(high,int(sum))
    low=min(low,int(sum))
print(high)
print(low)
    
