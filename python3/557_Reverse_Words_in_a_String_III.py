class Solution:
    def reverseWords(self, s: str) -> str:
        newS = [word[::-1] for word in s.split(" ")]
        return " ".join(newS)
