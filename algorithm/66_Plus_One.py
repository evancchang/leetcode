class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            else:
                return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
            return digits

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for digit in digits:
            total = total*10 + digit

        total += 1
        ans = []
        for d in str(total):
            ans.append(int(d))
        return ans
