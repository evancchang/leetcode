class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(columnTitle)
        total = 0
        for i in range(n-1, -1, -1):
            total += (ord(columnTitle[-i-1]) - ord('A') + 1) * (26 ** i)
        return total

class Solution2:
    def titleToNumber(self, columnTitle: str) -> int:
        char_num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8,
                    'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
                    'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22,
                    'W':23, 'X':24, 'Y':25, 'Z':26}

        n = len(columnTitle)
        total = 0
        for i in range(n-1, -1, -1):
            total += char_num[columnTitle[-i-1]] * (26 ** i)
        return total

class Solution3:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        
        for i, ch in enumerate(columnTitle[::-1]):
            number += (ord(ch) - ord('A') + 1) * (26**i)
        return number
