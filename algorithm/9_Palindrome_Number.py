class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        if x == 0:
            return True
            
        if x > 0:
            tmp = x
            reverse = 0
            
            # calculate the reverse number
            while tmp:
                reverse = reverse*10 + tmp%10
                tmp /= 10
                
            return reverse == x
