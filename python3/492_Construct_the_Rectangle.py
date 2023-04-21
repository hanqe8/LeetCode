class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for j in range(int(area**0.5),0,-1):
            if area % j == 0:
                return [area//j,j]
