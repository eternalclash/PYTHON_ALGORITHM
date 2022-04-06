d=[0]*10000
d[1]=1
d[2]=3
for i in range(3,10000):
    d[i]=d[i-1]+d[i-2]*2

print(d[3])