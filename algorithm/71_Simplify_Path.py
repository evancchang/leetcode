class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack = []
        
        for ch in path_list:
            if ch == '' or ch == '.' or ch == '..' and not stack:
                continue
            elif ch == '..' and stack:
                stack.pop()
            else:
                stack.append(ch)
        
        return '/' + '/'.join(stack)
        
