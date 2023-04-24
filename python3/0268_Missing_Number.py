class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Create a set of all numbers in the range [0, n] and find the difference between that set and the set of numbers in nums
        new_set = set(range(len(nums)+1))
        list(new_set - set(nums))[0]
        # Alternatively, use XOR
        missing_num = len(nums)
        for i, num in enumerate(nums):
            missing_num ^= i ^ num
        return missing_num
