class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                product *= -1
        return product
