from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        
        for s in strs:
                ans_dict[tuple(sorted(s))].append(s)
                
        return ans_dict.values()

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        ans = []
        for str in strs:
            if tuple(sorted(str)) not in anagram_map:
                anagram_map[tuple(sorted(str))] = [str]
            else:
                anagram_map[tuple(sorted(str))].append(str)
                
        for k, v in anagram_map.items():
            ans.append(v)
            
        return ans
        
