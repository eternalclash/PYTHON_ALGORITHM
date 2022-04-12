n = int(input())
arr = set(map(int,input().split()))

target=1
for y in arr :
    if target < y :
        break
    target+=y
print(target)
