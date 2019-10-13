class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_list:
            self.min_list.append(x)
        elif x <=  self.min_list[-1]:
            self.min_list.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_list[-1]:
            self.min_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
