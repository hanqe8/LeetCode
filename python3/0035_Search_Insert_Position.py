class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            min, max = 0, len(nums)
            while min < max:
                mid = (min + max)//2
                if target > nums[mid]:
                    min = mid + 1
                else:
                    max = mid
        return min
