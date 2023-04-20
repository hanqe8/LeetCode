class Solution:
    def countSegments(self, s: str) -> int:
        if len(set(s.replace(" ", ""))) < 1:
            return 0
        count = sum([1 for i in s.strip(" ").split(" ") if i != ""])
        return count
