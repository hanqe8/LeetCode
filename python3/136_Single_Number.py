class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        soln = 0
        for i in nums:
            soln ^= i
        return soln
