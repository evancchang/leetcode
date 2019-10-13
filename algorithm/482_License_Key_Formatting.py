class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        S = S.replace('-', '')
        ns = len(S)
        sk = ns % K
        ans_list = []
        
        if sk != 0:
            ans_list.append(S[:sk])
            for i in range(sk, ns, K):
                ans_list.append(S[i:i+K])
        else:
            for i in range(0, ns, K):
                ans_list.append(S[i:i+K])
                
        return '-'.join(ans_list)
        
