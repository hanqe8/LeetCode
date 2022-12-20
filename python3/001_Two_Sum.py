class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i, value in enumerate(nums):
            objective = target - nums[i]
            if objective in seen_dict:
                return [i, seen_dict[objective]]
            else:
                seen_dict[value] = i
