import sys
N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
h=-1
for i in range(1,N):
    if arr[i]*arr[i-1] < 0:
        h=i
        break
if N==1:
    if arr[0]>0:
        print(arr[0])
    else:
        print(-1*arr[0])
    sys.exit()
def choose (array,n):
    result=0
    index=0
    while len(array)>=n:
        result+=2*array[index]
        del array[index:index+n]
    if array:
        result+=2*array[0]
    return result
if h!=-1:
   minus= arr[:h]
   plus=arr[h:]
   plus.reverse()
else:
    if arr[0]>0:
        arr.reverse()
        print(-arr[0]+choose(arr,M))
        sys.exit()
    else :
        print(arr[0]+-choose(arr,M))
        sys.exit()
        

if -1*minus[0]>plus[0]:
    max=minus[0]
else:
    max=-1*plus[0]


print(-1*choose(minus,M)+choose(plus,M)+max)




 

