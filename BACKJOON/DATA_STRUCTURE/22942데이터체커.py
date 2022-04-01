import sys
n = int(input())
circle = []
stack =[]
for i in range(n):
    d,r=map(int,input().split())
    circle.append((d-r,i,0))
    circle.append((d+r,i,1))
circle.sort()

for i in range(len(circle)):
    if circle[i][2] == 0 :
        stack.append(circle[i])
    else :
        if stack[-1][2] == 0:
            if circle[i][1] == stack[-1][1]:
               stack.pop()
            else:
                print("NO")
                break
print("YES")









































# for i in range(len(arr)):
#     for j in range (i+1,len(arr)):
#         d = abs(arr[i][0]-arr[j][0])
#         r = arr[i][1]+arr[j][1]
#         mr = abs(arr[i][1]-arr[j][1])
#         if d==0 or d<mr or r < d :
#             continue
#         else :
#             answer = False
#             break

# if answer : print("YES")
# else : print("NO")