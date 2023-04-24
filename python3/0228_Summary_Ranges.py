class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output, start, end = [], 0, 0
        while start < len(nums) and end < len(nums):
            if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
                end += 1
            elif start == end:
                output.append(str(nums[start]))
                start += 1
                end += 1
            else:
                output.append(str(nums[start])+"->"+str(nums[end]))
                start = end+1
                end += 1
        return output
