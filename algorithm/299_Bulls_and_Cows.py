class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s_dict = {}
        g_dict = {}
        bulls = cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]: 
               bulls += 1
            else:
                if secret[i] not in s_dict:
                    s_dict[secret[i]] = 1
                else:
                    s_dict[secret[i]] += 1
                    
                if guess[i] not in g_dict:
                    g_dict[guess[i]] = 1
                else:
                    g_dict[guess[i]] += 1   
                    
        for key in s_dict.keys():
            if key in g_dict.keys():
                cows += min(s_dict[key], g_dict[key])
                
        return "{}A{}B".format(bulls,cows)
