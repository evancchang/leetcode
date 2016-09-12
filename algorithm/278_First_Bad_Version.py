# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isBadVersion(n):
            return 0

        left = 1
        right = n

        while left <= right:
            mid = (left+right)/2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
