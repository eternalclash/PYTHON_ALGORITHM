# n = int(input())
# arr = list(input().split())
# col_stack=[]
# row_stack=[]
# for a in arr:
#     if a =="R" :
#         row_stack.append("R")
#     elif len(row_stack)!=0 and a=="L":
#         row_stack.pop()
#     elif a=="D":
#         col_stack.append("D")
#     elif len(col_stack)!=0 and a=="U":
#         col_stack.pop()
#     else:
#         continue
# print(len(row_stack)+1,len(col_stack)+1)
# 구현으로 풀어보자
n = int(input())
x, y = 1, 1
plans = input().split()
move_type=['L','R','U','D']
direction=[(0,-1),(0,1),(-1,0),(1,0)]
for i in range(n):
    for j in range(4):
        if i==move_type[j]:
            dx=x+direction[i][0]
            dy=y+direction[i][1]
            if dx<0 or n<dx or dy<0 or n<dy:
                continue
            x,y=dx,dy
print(dx,dy)        