class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j,ch in enumerate(row):
                if ch != '.':
                    # record the place

                    # i -> .87654321
                    # i -> 2........
                    #      ^
                    #      j

                    seen += [(ch,j),(i,ch),(i/3,j/3,ch)]

        return len(seen) == len(set(seen))

t = Solution()
print t.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
