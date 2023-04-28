class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        soln = []
        for i in range(left, right+1):
            if '0' in str(i): # since self-dividing number cannot contain 0, continue to next i
                continue
            value = i 
            while value > 0:
                n = value % 10 # obtain the last digit of i
                if i % n != 0: # check if i is not multiple of n then change value to -1 -> means it is not self-dividing
                    value = -1
                value = value//10 # if i multiple of n = self-divisible -> remove last digit of value (shorten the number)
            if value != -1:
                soln.append(i)
        return soln
