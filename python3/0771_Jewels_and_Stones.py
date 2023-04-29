class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel, stone = [], []
        stone[:0], jewel[:0] = stones, jewels # convert each string to list via string slicing
        return sum(i in jewel for i in stone) # for each element in jewel, check if exists in stones, if yes = +1, return total sum
