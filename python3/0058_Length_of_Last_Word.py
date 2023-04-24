class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i, word in enumerate(s[::-1].split()):
            if word == " ":
                next
            else:
                return len(word)
