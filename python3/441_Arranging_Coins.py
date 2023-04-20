class Solution:
    def arrangeCoins(self, n: int) -> int:
        # quadratic eqn: 1 + 2 + ... + k = (1 + k) * k / 2 = n
        # k^2 + k - 2n -> k = -1 +/- sqrt(1+8n)/2
        return int((-1 + (1+8*n)**0.5)//2)
        
        # using for loop:
        if n == 1: # if 1 coin -> 1 row
            return n
        for i in range(1, n+1): # loop by no. of coins
            n -= i # increment i by 1 each time to correspond to no. of coins in subsequent rows (1, 2, 3 ...)
            if n < 0: # once n becomes negative, return i - 1 rows
                return i-1
