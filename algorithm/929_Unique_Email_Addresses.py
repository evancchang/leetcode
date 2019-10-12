class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = []
        for email in emails:   
            email_list = email.split('@')
            local_name = email_list[0]
            domain_name = email_list[1]
        
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            
            real_email = local_name + '@' + domain_name
            if real_email not in ans:
                ans.append(real_email)
                       
        return len(ans)
        
