class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I':1, 'V':5, 'X':10,
                       'L':50, 'C':100, 'D':500, 'M':1000}
        
        n = len(s)
        total = roman_to_int[s[n-1]]
        for i in range(n-1, 0, -1):
            curr = roman_to_int[s[i]]
            prev = roman_to_int[s[i-1]]
            if curr <= prev:
                total += prev
            else:
                total -= prev

        return total
