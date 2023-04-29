class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
    
        # explanation of question from user: meanup (https://leetcode.com/meanup/)
        # If bits[i] == 0, then the last character must be a one-bit character, because a two-bit character cannot start with 0.
        # If bits[i] == 1, then the last character must be a two-bit character, because a one-bit character cannot start with 1.
        # In this case, we need to skip the next character, because it belongs to the two-bit character.
        # Continue traversing the array using the above two steps until you reach the beginning of the array or find a character that violates the above rules.
        # At the end of the traversal, if not violated any of the above rules, then the last character must be a one-bit character, and return true, else false.
        # can ignore last int in bits list as stated by question -> last int is always 0
        
        solnBool = True
        for i in (bits[-2::-1]):
            if i == 1:
                solnBool = not solnBool # reverse boolean if i == 1
            else:
                break # exit for loop
        return solnBool
