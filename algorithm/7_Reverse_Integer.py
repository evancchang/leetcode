class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x = abs(x)

        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x /= 10

        reverse_out = sign *ans

        if  ((reverse_out > 2147483647)or(reverse_out < -2147483648)): # handle 32-bit overflow            
            return 0
        else:
            return reverse_out

class Solution2:
    def reverse(self, x: int) -> int:
        if x > 0:
            signed = 0
        else:
            signed = 1
            x = abs(x)
            
        x_str = str(x)
        x_list = [x for x in x_str]
        x_list.reverse()
        
        x_str = ''.join(x_list)
        x = int(x_str)
          
        if signed == 1:
            x = -x
    
        if -2 ** 31 <= x <= (2 ** 31 - 1):
            return x
        else:
            return 0        
        
