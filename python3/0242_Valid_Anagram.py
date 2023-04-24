class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return all([False if s.count(i) != t.count(i) else True for i in set(s)])
