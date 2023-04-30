class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return str(0) # account for num == 0
        originalNum, soln = num, []
        if num < 0:
            num = -num # for negative numbers, convert to positive then convert to base 7
        while num:
            # conversion to base 7 (or replace 7 with any number to convert to other base)
            soln.append(str(num % 7)) # find remainder and append to soln to create binary
            num //= 7
        if originalNum >= 0:
            return ''.join(soln[::-1])
        else:
            return "-"+ "".join(soln[::-1]) # if originalNum is negative, add negative sign for base 7
