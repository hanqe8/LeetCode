class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        return any((nums[i] in my_dict and abs(i - my_dict[nums[i]]) <= k, my_dict.update({nums[i]: i}))[0] for i in range(len(nums)))
