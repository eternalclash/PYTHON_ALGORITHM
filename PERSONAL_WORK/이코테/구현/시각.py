# 초 = 3, 13, 23, 33, 43, 53,30 =>힌시간 420-49= 371
# 분 = 3, 13, 23, 33, 43 ,53.30 =>한시간당 420
# 시 = 3 => 3600
h= int(input())
answer=0
for i in range(60):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j)+str(k):
                answer+=1

print(answer)
