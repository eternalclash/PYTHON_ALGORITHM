from ntpath import join


n = list(input())
n = sorted(n)
s=0
print(n)
for i in range (len(n)-1):
    if n[i].isdigit():
        s+=int(n[i])
    else:
        n=n[i:]
        break
    

print("".join(n)+str(s))