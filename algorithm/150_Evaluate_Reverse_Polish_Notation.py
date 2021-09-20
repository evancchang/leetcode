class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        stack = []
        
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(left+right)
                elif token == '-':
                    stack.append(left-right)
                elif token == '*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right)) # for divide negative number, we neeed to use int(left/right) to instead of left//right
                    
        return stack.pop()
        
