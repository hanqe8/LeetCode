class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 0:
      return 0
    if x < 4:
      return 1
    i = 2 * self.mySqrt(x / 4)
    if (i + 1) * (i + 1) <= x and (i + 1) * (i + 1) >= 0:
      return i + 1
    return  i
      
#def mySqrt(self, x: int) -> int:
    #return int(x**0.5)
