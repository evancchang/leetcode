class Solution:
    def isValid(self, s: str) -> bool:
        ch_map = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in ch_map.keys():
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if ch_map[stack.pop()] != ch:
                    return False
                
        return not stack
