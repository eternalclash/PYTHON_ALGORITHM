## 들어오는 요소들을 a-z 정렬해서 obj에다가 넣어서 보여주면 끝
## 19m 23s

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	    tmp_dict ={}
	    for v in strs:
		    if str(sorted(v)) in tmp_dict:
			    tmp_dict[str(sorted(v))] += [v]
		    else:
			    tmp_dict[str(sorted(v))] = [v]
	    return tmp_dict.values()