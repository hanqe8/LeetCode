class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in format(n, 'b').zfill(32) if i == '1'])
