n,k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2=  list(map(int, input().split()))
arr1=sorted(arr1)
arr2=sorted(arr2)
print(arr1)
for i in range(k):
    arr1[i],arr2[len(arr2)-1-i]=arr2[len(arr2)-1-i], arr2[i]

print (sum(arr1))