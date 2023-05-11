class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum, bobSum = sum(aliceSizes), sum(bobSizes) # assign variables for sum of each person
        diff = (aliceSum - bobSum)//2
        anchor, pointer = 0, 0
        aliceSizes.sort(); bobSizes.sort()
        while anchor < len(aliceSizes) and pointer < len(bobSizes):
            temp = aliceSizes[anchor] - bobSizes[pointer]
            if temp == diff:
                return [aliceSizes[anchor], bobSizes[pointer]]
            elif temp < diff:
                anchor += 1
            else:
                pointer += 1
