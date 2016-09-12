class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return True

        s = s.lower()
        new_str = ""

        # +++ The following will cause time exceed limit +++
        #for char in s:
        #    if (('0'<=char<='9')or('a'<=char<='z')):
        #        new_str += char
        # --------------------------------------------------

        new_str = ''.join([char for char in s if ('0'<=char<='9')or('a'<=char<='z')])

        if new_str[::-1] == new_str:
            return True
        else:
            return False

t = Solution()
print t.isPalindrome("A man, a plan, a canal: Panama")
