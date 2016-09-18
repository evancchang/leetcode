class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = bin(n)[2:] # remove 0b
        out = out.zfill(32) # fill up to 32 bits
        out = out[::-1] # reverse bits
        out = int(out, 2)

        return out

t = Solution()
print t.reverseBits(43261596)
