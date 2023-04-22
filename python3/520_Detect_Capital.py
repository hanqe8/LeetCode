class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        elif word[:1].isupper() and word[1:].islower():
            return True
        else:
            return False
