import copy
s = list(map(str,input()))
answer = s[0]

# operator=["*","+"]
result=[]
def dfs(arr,n):
    if n == 0 : 
        result.append(copy.deepcopy(arr))
        return
    arr.append("+")
    dfs(arr,n-1)
    arr.pop()

    arr.append("*")
    dfs(arr,n-1)
    arr.pop()

dfs([],len(s)-1)
m=0
for result in result:
    letter =s[0]
    for i in range(len(result)):
        letter=letter+result[i]+s[i+1]
    m=max(m,eval(letter))

print(m)
        


## 문자열 12345를 정수로 쪼개려면 제일 간단한 것은 그냥 통쨰로 다받고 list로 쪼개면된다
