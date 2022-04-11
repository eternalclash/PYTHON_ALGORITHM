n = int(input())

arr = list(map(int,input().split()))

obj = {}
answer =0
for i in range(len(arr)):
    try : 
        obj[arr[i]]+=1

    except :
        obj[arr[i]]=1
    if obj[arr[i]]==arr[i]:
        answer+=1
print(answer)