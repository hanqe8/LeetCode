class Solution:
    def findComplement(self, num: int) -> int:
        newNum, numDict = '', {"0": "1", "1": "0"} # create dictionary reference to reverse numbers
        for i in str(bin(num)[2:]): # use in-built function bin to convert int to binary (0b...) and slice to obtain int only
            newNum += numDict[i] # iterate through string provided and join corresponding key-value from dict
        return int(newNum, 2) # convert binary string back to int, base 2
