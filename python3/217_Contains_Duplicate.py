class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        return any([True if i in my_set else my_set.add(i) for i in nums])
