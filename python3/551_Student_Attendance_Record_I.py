class Solution:
    def checkRecord(self, s: str) -> bool:
        if Counter(s)['A'] < 2 and 'LLL' not in s:
            return True
        else:
            return False
