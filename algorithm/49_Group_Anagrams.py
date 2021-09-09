from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        
        for s in strs:
                ans_dict[tuple(sorted(s))].append(s)
                
        return ans_dict.values()
