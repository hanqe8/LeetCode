class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        soln = []
        for email in emails:
            local, domain = email.split('@')[0], email.split('@')[1]
            if '+' in local:
                local = local.split('+')[0]
            if '.' in local:
                local = local.replace('.', '')
            soln.append(local+ '@' + domain)
        return len(set(soln))
