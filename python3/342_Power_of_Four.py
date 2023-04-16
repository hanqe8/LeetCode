class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # with recursion
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 4 == 0:
            return self.isPowerOfFour(n//4)
        return False
        
        # without recursion
        # n & (n-1) check for power of 2 to reject
        # n % 3 == 1 only true for power of 4 as 4**(x-1) always divisible by 3
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1 
