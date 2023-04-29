class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        numsList = sorted(nums, reverse=True) # create new list for sorted nums in descending order
        if numsList[0] >= 2 * numsList[1]:
            return nums.index(numsList[0]) # return index of largest int in nums if at least 2x of next largest number
        return -1
      
        # alternative method using enumerate
        first, second, max_idx = 0, 0, 0
        for idx, i in enumerate(nums):
            if i >= first:
                first, second = i, first # if i in nums larger than existing first -> replace existing first with i and replace existing second with first
                max_idx = idx # return the index of the current highest integer
            elif i > second: 
                second = i # if i larger than second only, replace second with i as next largest int
        if first >= 2 * second:
            return max_idx
        return -1
