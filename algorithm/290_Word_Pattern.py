class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False

        p_dict = {}

        for p, w in zip(pattern, words):
            if (p not in p_dict):
                if w not in p_dict.values():
                    p_dict[p] = w
                else:
                    return False

            else:
                if p_dict[p] != w:
                    return False

        return True

t = Solution()
print t.wordPattern('abba', 'dog dog dog dog')
