class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if len(Counter(set(candyType))) >= (len(candyType)/2):
            return len(candyType)//2
        else:
            return len(Counter(set(candyType)))
