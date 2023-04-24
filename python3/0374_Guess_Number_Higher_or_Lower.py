# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowerlimit, upperlimit = 1, n
        while upperlimit >= lowerlimit:
            mid = (lowerlimit + upperlimit) // 2
            soln = guess(mid)
            if soln < 0:
                upperlimit = mid-1
            elif soln > 0:
                lowerlimit = mid+1
            else:
                return mid 
