import collections
class Solution:
    def isValid(self, s: str) -> bool:
        ch_map = {')':'(', '}':'{', ']':'['}
        stack = collections.deque()
        
        for ch in s:
            if ch in ch_map.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if ch_map[ch] != stack.pop():
                    return False
                
        return not stack
                
