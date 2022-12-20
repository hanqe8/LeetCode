class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupes = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dupes += 1
            else:
                nums[i - dupes] = nums[i]
        return len(nums) - dupes
