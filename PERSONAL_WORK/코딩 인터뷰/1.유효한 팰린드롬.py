# 1. 리스트들을 입력받는다.
# 2. isalnum()==영문자,숫자 여부를 판별 | 영문자 숫자면 TRUE, 아니면 FALSE
# 3. 빈 배열에 추가
# 4. 배열의 길이가 1보다 클떄 
# 5. 배열.pop(0)==배열.pop() //배열.pop(0)은 배열의 첫 번째 요소를 파는 것!

def isPalindrome(self, s):
    strs = []
    for chars in s :
        if chars.isalnum() :
            strs.append(chars.lower())
    while len(strs) > 1 :
        if strs.pop(0) == strs.pop():
            continue
        else :
            return False
    return True
#1 리스트로 변환하기 ==내가 생각한 정답


#두번쨰 deque 큐를 사용한 최적화
def isPalidrome(self, s):
    strs:Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

#슬라이싱을 이용한 문제풀이 
def isPalindrome(self, s: str) -> bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s) #정규식으로 문자랑 숫자만 나오게 슬라이싱
    return s == s[::-1] #슬라이싱
    #s=[::-1] 문자열을 뒤집을 수 있음

#문자열을 다룰 땐 슬라이싱을 하는 것이 제일 빠르다 어떻게 해야 할지 생각해보자
# arr="안녕하세요" arr[::-1] 요세하녕안, arr[::2] 안하요 , arr[1:-2]안녕하 음수는 -1부터 [a:b]a에서b-1까지
