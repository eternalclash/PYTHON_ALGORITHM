import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
def solution(rc, operations):
    def shiftRow(x):
        l=len(x)
        r=len(x[0])
        arr=[[0]*r for _ in range(l)]
        for i in range(l):
            if i==0:
                arr[i]=x[l-1]
                continue
            arr[i]=x[i-1]
        return arr
    def rotate(x):
        temp=x[0][0]
        top, left, bottom, right = 0,0,len(x)-1,len(x[0])-1    
        for k in range(top, bottom):    
            x[k][left] = x[k + 1][left]
 
        for k in range(left, right):   
            x[bottom][k] = x[bottom][k + 1]
 
        for k in range(bottom, top, -1):   
            x[k][right] = x[k - 1][right]
 
        for k in range(right, left, -1):    
            x[top][k] = x[top][k - 1]
 
        x[top][left + 1] = temp    
        return x
    for i in range (len(operations)):
        if operations[i]=="Rotate":
            rc=rotate(rc)
        elif operations[i]=="ShiftRow":
            rc=shiftRow(rc)
    return rc

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate","Rotate","Rotate","Rotate","ShiftRow"]))