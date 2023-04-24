class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            total = sum([int(i) for i in str(num)])
            num = total
        return num
