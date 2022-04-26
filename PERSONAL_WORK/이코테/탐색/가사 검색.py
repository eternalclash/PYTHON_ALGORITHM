def find (words,query):
    arr=[]
    index=0
    count=0
    for i in range(len(query)):
        if query[i]!="?":
            arr.append([i,query[i]])
    print(arr)
    for word in words:
        if len(word)!=len(query):
            continue

        if len(arr)==0:
            count+=1
            continue
        t=True
        index=0
        for i in range(len(word)):
            if i==arr[index][0] and word[i]==arr[index][1]:
                index+=1
                if index==len(arr):
                    break           
                continue
            if i==arr[index][0] and word[i]!=arr[index][1]:
                t=False     
                break
        print(word)
        if t:
            count+=1
    return count
                
            
def solution(words, queries):
    answer=[]
    for query in queries:
        s=find(words,query)
        answer.append(s)
        
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))