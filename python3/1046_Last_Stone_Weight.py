class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones.remove(max(stones))
                stones.remove(max(stones))
            else:
                new_stone = max(stones[0:2]) - min(stones[0:2])
                stones.remove(max(stones))
                stones.remove(max(stones))
                stones.append(new_stone)
            stones = sorted(stones, reverse=True)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
