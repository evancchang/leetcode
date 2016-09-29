class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                if ch == ')':
                    if stack.pop() != '(':
                        return False
                if ch == '}':
                    if stack.pop() != '{':
                        return False
                if ch == ']':
                    if stack.pop() != '[':
                        return False
                    
        return not stack
