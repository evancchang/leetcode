class MyCircularQueue:

    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.size = 0
        self.max_size = k
        self.cq = [0] * k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.head == self.tail and self.head == -1: # when queue clear, move the pointer to the first
                self.head = self.tail = 0
            else:
                self.tail += 1
                self.tail %= self.max_size
            self.cq[self.tail] = value                
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head += 1
            self.head %= self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
