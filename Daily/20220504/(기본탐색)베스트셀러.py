N= int(input)
obj={}
for _ in range(N):
    x=input()
    try:
        obj[x]+=1
    except:
        obj[x]=1

answer=[]
target = max(obj.values()) ###포인트
for key,number in obj.items():
    if number == target:
        answer.append(key)

print(sorted(answer)[0])
    

    
