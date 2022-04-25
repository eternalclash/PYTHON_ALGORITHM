K = int(input())
stack=[]
for _ in range(K):
    n=int(input())
    if n==0:
        stack.pop()
    else:
        stack.append(n)
if stack:
   print(sum(stack))
else:print(0)