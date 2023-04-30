class Solution:
    def calPoints(self, operations: List[str]) -> int:
        steps, final = [], 0
        for i in operations:
            if i == 'D':
                steps.append((steps[-1]) * 2)
                final += steps[-1]
            elif i == 'C':
                final -= steps.pop()
            elif i == '+':
                steps.append(steps[-1] + steps[-2])
                final += steps[-1]
            else:
                steps.append(int(i))
                final += steps[-1]
        return final
                
