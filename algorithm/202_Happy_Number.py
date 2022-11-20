class Solution:
    def isHappy(self, n: int) -> bool:
        repeat = set()

        while n != 1 and n not in repeat:
            repeat.add(n)
            curr_val = 0
            while n:
                curr_val += (n % 10) ** 2
                n //= 10
            n = curr_val

        return n == 1
