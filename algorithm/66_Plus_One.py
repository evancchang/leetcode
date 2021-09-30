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
        s = ''
        for d in digits:
            s += str(d)
        
        s = int(s) + 1
        ans = []
        for ch in str(s):
            ans.append(int(ch))
            
        return ans
