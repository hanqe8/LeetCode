class Solution:
    def canWinNim(self, n: int) -> bool:
        # self starts first and max draw = 3
        return n % 4 != 0 # check if divisible by 4, if possible = lose
