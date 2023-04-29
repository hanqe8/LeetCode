class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums) 
        for idx, i in enumerate(nums): # iterate through nums and enumerate to return position of left most index
            rightSum -= i # remove value of i from sum of nums
            if leftSum == rightSum:
                return idx # if pivot index exists = return idx (index of enum)
            leftSum += i # add on to leftSum
        return -1 # if no pivot index exists, return -1
