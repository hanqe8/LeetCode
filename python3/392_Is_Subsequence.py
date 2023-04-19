class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        count = 0
        for i in t:
            if i == s[count]:
                count += 1
            if count == len(s):
                break
        return count == len(s)
