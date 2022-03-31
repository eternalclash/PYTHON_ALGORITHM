#오랜만에 백준 골드도 쉽지않네 하
#괄호제거
#1. 스택으로 괄호 쌍끼리 튜플로 찾아서 배열의 ㅜ가
#2. 조합으로 배열의 쌍 다 쪼갬
#3. 중복되지 않게 set사용
# point 파이썬 튜플인 배열 for x,y in arr 이 형식 좀 생각하자 제발
# 문자형은 그리고 js처럼 순회할 수 없다

n = input()  #(0/(0))
left_stack=[]
gal=[]
final=set()
for i in range(len(n)):
    if n[i]=='(' :
        left_stack.append(i)
    elif n[i]==')' and len(left_stack) > 0 :
        gal.append((left_stack.pop(),i))
def combination (nums,n) :
    result = []
    if n==0 : return [[]]
    for i in range (len(nums)):
        fixed = nums[i]
        rest = nums[i+1:]
        for c in combination(rest,n-1):
            result.append([fixed]+c)
    return result
for i in range(1,len(gal)+1):
    answers=combination(gal,i)
    for answer in answers:
        temp=list(n)
        for left,right in answer:
            temp[left]=""
            temp[right]=""
        final.add("".join(map(str, temp)))
final = list(final)
final.sort()
for i in range(len(final)):
    print(final[i])





