# N, M = map(int,input().split()) # N= 볼링공의 개수 ,M=  1부터 M까지 무게

def combination (arr,n):
    result=[]
    if n==0: 
        return [[]]
    for i in range(0,len(arr)):
        fixed = arr[i]
        rest= arr[i+1:]
        for l in combination(rest,n-1):
            result.append([fixed]+l)
    return result

def count_combi(n,k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return count_combi(n-1,k)+count_combi(n-1,k-1)

print(count_combi(4,2))

