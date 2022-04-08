import copy
test_case=int(input())

def recursive(arr,n):
    if len(arr) == n:
        operator_list.append(copy.deepcopy(arr))
        return 
    
    arr.append(' ')
    recursive(arr,n)
    arr.pop()

    arr.append('+')
    recursive(arr,n)
    arr.pop()

    arr.append('-')
    recursive(arr,n)
    arr.pop()

for _ in range(test_case):
    operator_list=[]
    n=int(input())
    array=[]
    recursive([],n-1)
    for i in range (1,n+1):
        array.append(i)
    
    for operator in operator_list:
       string=""
       for i in range (n-1):
        string+=str(array[i])+operator[i]
       string += str(array[-1])
       if eval(string.replace(" ",""))== 0:
           print(string)
    print()


