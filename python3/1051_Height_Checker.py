class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, count = sorted(heights), 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        return count
