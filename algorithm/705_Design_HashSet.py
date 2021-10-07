class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def add(self, key: int) -> None:
        self.set.add(key)
        
    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.set:
            return True
        else:
            return False
        


class MyHashSet2:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        if key not in self.list:
            self.list.append(key)

    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.list        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
