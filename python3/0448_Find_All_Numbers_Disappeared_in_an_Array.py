class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # to return missing numbers in range for nums
        # highest int in nums is max of range -> range(1, len(nums) + 1) returns [1, x]
        # difference between sets will return missing numbers without duplicates
        return set(range(1, len(nums)+1)) - set(nums) # or use python set difference method -> return set(range(1, len(nums)+1)).difference(set(nums))
