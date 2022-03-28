def reorderLogFiles(self,logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

# 풀이방향
# 1. log.split()[1]이 숫자인 아닌지 => isdigit(),isalnum,isalpha 외웁시다
# 2. 그거에 대한 분기로 숫자배열, 문자배열로 넣은다음
# 3. 문자가 동일한 경우 식별자 순으로 정렬 정렬은 항상오름차순인거 같은데?