from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        counter = 0
        visited = set()
        q = deque(["0000"])
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node == target:
                    return counter
                elif node in deadends:
                    continue
                else:
                    for i, ch in enumerate(node):
                        num = int(ch)
                        temp1 = node[:i] + str((num + 1) % 10) + node[i+1:]
                        temp2 = node[:i] + str((num - 1) % 10) + node[i+1:]

                        if temp1 not in visited and temp1 not in deadends:
                            q.append(temp1)
                            visited.add(temp1)

                        if temp2 not in visited and temp2 not in deadends:
                            q.append(temp2)
                            visited.add(temp2)
            counter += 1 # Add 1 to steps to go to the next level as we were not able to find target in this level 
        return -1
