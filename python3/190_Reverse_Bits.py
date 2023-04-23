class Solution:
    def reverseBits(self, n: int) -> int:
        # since n is 32 bit unsigned integer
        # format n to binary using .format('b') and fill up leading 0s using .zfill(x) where x is total length of string
        # reverse string [::-1] and return corresponding int of base 2
        return int(format(n, 'b').zfill(32)[::-1], 2)
