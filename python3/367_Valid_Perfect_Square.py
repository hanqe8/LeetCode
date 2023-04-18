class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lowerLimit, upperLimit = 1, num
        while upperLimit >= lowerLimit:
            mid = (lowerLimit + upperLimit) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                upperLimit = mid - 1
            else:
                lowerLimit = mid + 1
        return False
