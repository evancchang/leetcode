class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in xrange(1, n):
            s = self.cal(s)            
        return s

    def cal(self, s):
        counter = 1

        tmp = s[0]
        out = ""

        for i in xrange(1, len(s)):
            if tmp == s[i]:
                counter +=1
            else:
                out += str(counter) + tmp
                counter = 1
                tmp = s[i]

        out += str(counter) + tmp
        return out

t = Solution()
print t.countAndSay(4)
