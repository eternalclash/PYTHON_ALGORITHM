from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram=defaultdict(list)  
        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return list(anagram.values())
# defaultdict활용하면 object 에러 발생 X
# list(anagram.values())이렇게 하면 value값들로만의 리스트가 형성됨
