class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer, count = None, 0
        for i in nums:
            if count == 0:
                answer = i
            count += 1 if i == answer else -1
        return answer
