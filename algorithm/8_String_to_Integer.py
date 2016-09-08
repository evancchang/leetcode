class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not len(str):
            return 0

        str = str.strip()
        if str[0] == '-':
            sign = -1
            str_num = str[1:]
        elif str[0] == '+':
            sign = 1
            str_num = str[1:]
        elif ('0'<=str[0]<='9'):
            sign = 1
            str_num = str
        else:
            return 0

        out_num = 0
        for char in str_num:
            if ('0'<=char<='9'):
                char2num = ord(char) - ord('0')
                out_num = out_num * 10 + char2num
            else:
                break

        out_num = sign * out_num
        if  out_num > 2147483647:
            return 2147483647
        elif out_num < -2147483648:
            return -2147483648
        else:
            return out_num
