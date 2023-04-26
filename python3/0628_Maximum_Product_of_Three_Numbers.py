class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # since -1000 <= nums[i] <= 1000 and max product of 3 int
        # check max of (2 -ve num * 1 +ve num OR 3 +ve num) after sorting in ascending order
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        
