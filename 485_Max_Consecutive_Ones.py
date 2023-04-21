class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

      # using for loop (results in time exceeded error if nums too long)
      numsLength, indexList = len(nums), []
      count = 65 # set base count for ASCII character
      if len(set(nums)) == 1 and Counter(set(nums))[1] == 0: # for nums == [0]
        return 0
      for i in range(numsLength): # iterate through nums and append corresponding ASCII character if "1" and "0" if "0" -> [1, 1, 0, 1] == [a, a, 0, b]
        if nums[i] == 0:
          indexList.append(nums[i])
          count += 1
        else:
          indexList.append(chr(count))
      return Counter(indexList)[max(indexList, key=indexList.count)] # return the highest count (consecutive count) ASCII character

      # using for loop
      count = result = 0
      for i in nums: # iterate through nums and assign values to count and result
        count = count * i + i # count resets if passes through 0
        result = max(result, count) # where new result = max value between result and count
      return result
