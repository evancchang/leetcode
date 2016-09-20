class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_length = len(strs[0])
        prefix = strs[0]
        if not min_length:
            return ""

        min_index = 0
        for i in xrange(len(strs)):
            if min_length > len(strs[i]):
                min_length = len(strs[i])
                min_index = i
                prefix = strs[i]

        if len(strs) < 2:
            return prefix
        else:
            strs.remove(prefix)

        idx = -1
        compare = True

        for i in xrange(len(prefix)):
            for word in strs:
                if compare:
                    if prefix[i] != word[i]:
                        compare = False
            if compare: # record the prefix index
                idx = i

        if idx != -1:
            return prefix[0:idx+1]
        else:
            return ""

t = Solution()
#print t.longestCommonPrefix(['awbc', 'ab', 'aebcde'])
print t.longestCommonPrefix(['a', 'a', 'b'])
