steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
data=input()
row= int(data[1])
answer = 0
column = int(ord(data[0]))- int(ord('a')) + 1
for step in steps:
    dr = row + step[0]
    dc = column + step[1]
    if 1<dr<=8 and 1<dc<=8 :
        answer+=1
print(answer)
#ord(문자 반환)
