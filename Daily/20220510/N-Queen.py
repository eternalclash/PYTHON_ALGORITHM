#기본적인 백트래킹은 dfs로 탐색하는 것이 좋다
#다시 풀기에도 좋은문제


def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    if x==n:
        result+=1
    else:
        for i in range(n):
            row[x] =i
            if check(x):
                dfs(x+1)

n=int(input())
row= [0] * n
result = 0
dfs(0)
print(result)