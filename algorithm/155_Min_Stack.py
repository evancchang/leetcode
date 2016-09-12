class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_val:
            if self.min_val[-1] >= x:
                self.min_val.append(x)
        else:
            self.min_val.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.min_val[-1] == self.stack[-1]:
                self.min_val.pop()

            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(2)
obj.push(3)
obj.push(1)
obj.push(4)
print obj.top()
print obj.getMin()
obj.pop()
obj.pop()
print obj.getMin()
