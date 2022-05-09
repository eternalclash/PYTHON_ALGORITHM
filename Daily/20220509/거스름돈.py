s=1000-int(input())
count =0
for i in [500,100,50,10,5,1]:
    count += s//i
    s=s%i
print(count)
    
    