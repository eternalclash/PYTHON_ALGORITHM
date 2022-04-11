obj={0:0,1:0}
arr = list(map(int,input()))
for i in range(len(arr)):
    if i==0:
        continue

    if i==len(arr)-1:
        obj[arr[i]]+=1

    if arr[i]==arr[i-1]:
        continue
    else :
        obj[arr[i-1]]+=1

print(min(obj[0],obj[1]))

