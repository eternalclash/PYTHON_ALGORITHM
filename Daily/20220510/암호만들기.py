import copy
L,C = map(int,input().split())
arr=list(map(str,input().split()))
answer=[]
check=["a","e","i","o","u"]
def find(index,a,b,stack):
    if a>=1 and b>=2 and a+b==L:
        stack.sort()
        answer.append(copy.deepcopy("".join(stack)))
        return
    if index==C:
        return
    
    if arr[index] in check:
        find(index+1,a+1,b,stack+list(arr[index]))
    else:
        find(index+1,a,b+1,stack+list(arr[index]))
    find(index+1,a,b,stack)

find(0,0,0,[])
answer=sorted(answer)
for i in range(len(answer)):
    print(answer[i])






    