class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
                
        if carry == 1:
            digits.insert(0, 1)
            
        return digits

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 1
        n = len(digits)
        
        for i in range(n-1, -1, -1):
            total += digits[-i-1] * (10**i)
            
        total_list =[]
        for digit in str(total):
            total_list.append(int(digit))

        return total_list
