class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1: return 1 # handle single character cases
        sSet = set()
        for i in s: # run through all alphabets in str and add into set if does not exist in set else remove
            if i not in sSet:
                sSet.add(i)
            else:
                sSet.remove(i)
        # sSet now contains all unpaired alphabets from str
        if len(sSet) != 0:
            return len(s) - len(sSet) + 1
        else:
            return len(s) # if no unpaired alphabets, longest palindrome = entire str
