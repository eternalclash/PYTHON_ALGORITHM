# 하,,,시간복잡도O(N**2)라서 안되네,,, 꽁문제인줄 알았다,,
# n = int(input())
# arr = list(map(int,input().split()))
# answer = [0]
# for i in range(1,len(arr)):
#     k=True
#     for j in range(i-1,-1,-1):
#         if arr[i]<=arr[j]:
#             answer.append(j+1)
#             k=False
#             break
#         else:continue
#     if k :
#         answer.append(0)
# print (" ".join(map(str,answer)))


n= int(input())
arr = list(map(int,input().split()))
stack=[]
answer=[]
for i in range(len(arr)):
    while stack:
        if stack[-1][1]>arr[i]:
            answer.append(stack[-1][0]+1)
            break
        else :
            stack.pop()
    if len(stack)==0:
        answer.append(0)
    stack.append([i,arr[i]])

print (" ".join(map(str,answer)))
    