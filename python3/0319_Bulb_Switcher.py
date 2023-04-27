class Solution:
    def bulbSwitch(self, n: int) -> int:
        # r1: i
        # r2: i o
        # r3: i o o
        # r4: i o o i
        # r5-9: i o o i o, i o o i o o, i o o i o o o, i o o i o o o o, i o o i o o o o i
        return int(sqrt(n))
