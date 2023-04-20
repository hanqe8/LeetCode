class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numberDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        def dumpFunc(num):
            soln = 0
            for i in num:
                soln = soln * 10 + numberDict[i]
            return soln
        return str(dumpFunc(num1) + dumpFunc(num2))
