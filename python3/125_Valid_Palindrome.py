import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'\W+', '', s).lower().replace('_','')
        return new_s == new_s[::-1]
