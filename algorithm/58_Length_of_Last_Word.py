class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        s = s.split()
        if s:
            return len(s[-1])
        else:
            return 0
