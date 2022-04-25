N= int(input())
i=0
stack=[0]
arr=[]
t=True
for _ in range(N):
    x=int(input())
    while i<x:
        i+=1
        arr.append("+")
        stack.append(i)
    
    if stack[-1]==x:
        arr.append("-")
        stack.pop()
    else:
        t=False

if not t:
    print("NO")
else:
    for i in range(len(arr)):
        print(arr[i])
        




    
    
