class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ''
        curr_num = 0
        
        for ch in s:
            if ch == '[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ''
            elif ch == ']':
                prev_str = stack.pop()
                num = stack.pop()
                curr_str = prev_str + num*curr_str
            elif ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            else:
                curr_str += ch
                
        return curr_str
        
