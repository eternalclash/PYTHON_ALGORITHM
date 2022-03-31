n = int(input())
arr = list(input().split())
col_stack=[]
row_stack=[]
for a in arr:
    if a =="R" :
        row_stack.append("R")
    elif len(row_stack)!=0 and a=="L":
        row_stack.pop()
    elif a=="D":
        col_stack.append("D")
    elif len(col_stack)!=0 and a=="U":
        col_stack.pop()
    else:
        continue
print(len(row_stack)+1,len(col_stack)+1)
    