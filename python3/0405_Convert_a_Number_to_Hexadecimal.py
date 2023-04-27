class Solution:
    def toHex(self, num: int) -> str:
        soln, mapping = '', '0123456789abcdef' # mapping for hexadecimal characters
        if num == 0: # account for num == 0
            return '0'
        if num < 0: # use two's complement method to convert o +ve
            num += 2**32
        while num > 0: # repeat new num till 0
            remainder = (num%16) #obtain remainder left from dividing by 16
            soln += str(mapping[remainder]) # map remainder to hexadecimal char
            num = num//16
        return soln[::-1] # return reversed string
