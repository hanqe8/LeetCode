class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        else:
            nums = set(nums)
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
