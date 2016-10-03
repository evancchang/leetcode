class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = cow = 0
        s_dict = {}
        g_dict = {}
        
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                # use dict to calculate the value number.
                if secret[i] not in s_dict:
                    s_dict[secret[i]] = 1
                else:
                    s_dict[secret[i]] += 1
                    
                if guess[i] not in g_dict:
                    g_dict[guess[i]] = 1
                else:
                    g_dict[guess[i]] += 1
                    
        for key in s_dict:
            if key in g_dict:
                cow += min(s_dict[key], g_dict[key])
                
        return "%sA%sB" %(bull, cow)
