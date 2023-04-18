class Solution:
    def reverseVowels(self, s: str) -> str:
        slist, vowels, slow, fast = list(s), "AaEeIiOoUu", 0, len(s)-1
        while fast > slow:
            if slist[slow] in vowels and slist[fast] in vowels:
                slist[slow], slist[fast] = slist[fast], slist[slow]
                slow += 1
                fast -= 1
            elif slist[slow] not in vowels:
                slow += 1
            elif slist[fast] not in vowels:
                fast -= 1
        return "".join(slist)
