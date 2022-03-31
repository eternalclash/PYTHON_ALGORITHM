#Data Cleansing을 해야하는 데 정규식 섞어 쓰는게 너무나도 불편하다
#지금도 해설 풀이가 이해가 안된다 일단 PASS
def mostCommonWord(self,paragraph,banned):
    words= [word for word in re.sub(r'[^\w]',' ', paragraph)
      .lower().split() 
    if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]